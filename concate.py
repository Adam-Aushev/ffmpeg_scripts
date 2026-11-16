import os
from os.path import join as pathjoin
import shutil
import sys
import subprocess


class bcolors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_format(link):
    vformats = ['.mp4', '.mov']
    if os.path.splitext(link)[1] in vformats:
        return True
    else:
        return False


    
def progress_bar( prog, volume, info=''):
    progress =int( prog*(100/volume))
    probar = f"[{progress*'#' + (99 - progress)*'.'}]"
    sys.stdout.write('\r'+ info+'  '+probar)

def get_export_folder(link):
    if os.name == 'nt':
        drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
        for dr in drives:
            for fold in os.listdir(f'{dr}\\\\'):
                if 'export' in fold.lower():
                    exp_folder = pathjoin(dr, fold)
    else:
        exp_folder = '/home/dell_ubuntu/export'
    os.mkdir(exp_folder) if not os.path.isdir(exp_folder) else 1
    if 'split' in ''.join(sys.argv):
        dir_name = link.replace('\\', '_').replace(' ', '_').replace(':', '').replace('/', '_')
        exp_folder = pathjoin(exp_folder, dir_name)
    else:
        exp_folder = pathjoin(exp_folder, 'Convert')
        # if os.path.isdir(exp_folder):
        #     shutil.rmtree(exp_folder) # del convert folder
    os.mkdir(exp_folder) if not os.path.isdir(exp_folder) else 1 
    print(exp_folder)
    return exp_folder


def get_dur(link, shape=True):
    shapeform = ''
    if shape == True:
        shapeform = '-sexagesimal'
    code = f'ffprobe -v error -show_entries format=duration {shapeform} -of default=noprint_wrappers=1:nokey=1 "{link}"'
    cmd = f'{code}'
    timecode = ''
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                               stderr=subprocess.STDOUT, universal_newlines=True, encoding='utf-8', shell=True)
    for line in process.stdout:
        timecode += line
    return line.strip()


def create_sub(link, source_name, each_num, source_path):
    file_name = os.path.split(link)[1]
    sub_path = pathjoin(source_path, f'{os.path.splitext(file_name)[0]}.srt')
    timecode = get_dur(source_name).replace('.', ',')[:11]
    subtitle = f'1\n00:00:00,000 --> 0{timecode}\n{file_name}\n\n'
    with open(sub_path, 'w', encoding='utf-8') as subfile:
        subfile.write(subtitle)
    return sub_path


def get_compare(source_file, exp_file):
    status = f'{bcolors.GREEN}Yes{bcolors.END}' 
    src_dur = float(get_dur(source_file, shape=False))
    exp_dur = float(get_dur(exp_file, shape=False))
    if src_dur - exp_dur == 0:
        return f'{bcolors.GREEN}{source_file}{src_dur} = {exp_dur} YES'
    else:
        return f'{bcolors.RED}{source_file}{src_dur} != {exp_dur} No'


if '-h' in ''.join(sys.argv) or 'help' in ''.join(sys.argv):
    print('h265 - render with hevc')
    print('split - render split clips in folder')
    print('nolut - render without lut')
else:
    os.system('nano concate_links.txt')
    with open('concate_links.txt', 'r', encoding='utf-8') as link_file:
        for link in link_file:
            link = link.strip()
            exp_folder = get_export_folder(link)
            link_split = link.split("\\")
            for link_peace in reversed(link_split):
                if 'сони' not in link_peace.lower()   and 'коп' not in link_peace.lower()   and 'кенон' not in link_peace.lower()  and 'видео' not in link_peace.lower()  :
                    if link_peace != link_split[-1]:
                        file_name = f'{link_peace}_{link_split[-1]}'
                    else:
                        file_name = link_peace   
                    break   
                
            video_list = ''    
            list_files = os.listdir (link)  
            # print(list_files)
            countdown =0
            for each_file in list_files:
                countdown += 1
                subtitle = ''
                if '.mp4'in each_file.lower() or '.mov' in each_file.lower() or '.braw' in each_file.lower():
                    filters = ''
                    video_list += f"file '{each_file}'\n"
                    if not 'nolut' in ''.join(sys.argv):
                        filters = "scale=1920:1080"
                        filters += ", lut3d=luts//LC-709_.cube"
                        filters = f'-vf "{filters}"'
                        # filters += ", lut3d=luts//From_SLog2SGumut_To_SLog2-709_.cube"
                    if 'h265' in ''.join(sys.argv):
                        vcodec = '-c:v libx265 -vtag hvc1' 
                    else:
                        vcodec = '-c:v h264 -profile:v baseline'
                    end_file = f"{os.path.splitext(each_file)[0]}.mp4"

                    end_name = pathjoin(exp_folder, end_file)
                    title_name = create_sub(end_name, pathjoin(link, each_file), list_files.index(each_file), exp_folder)
                    print(get_compare(pathjoin(exp_folder, each_file), end_name))
                    if 'split' not in ''.join(sys.argv):
                        subtitle = f' -c:s mov_text -metadata:s:s:0 handler_name="Таймкоды"' 
                    if end_file not in os.listdir(exp_folder):
                        each_convert = f'ffmpeg -v error -stats  -i "{pathjoin(link, each_file)}" -i "{title_name}" -x265-params log-level=none -c:a aac -rf64 auto {vcodec} -preset ultrafast  -pix_fmt yuv420p -crf 25 {filters} {subtitle} -y "{end_name}"'
                        progress_bar(countdown, len(list_files), info=f'rendering - {each_file} {countdown} in {len(list_files)}')
                        os.system(each_convert)
            if 'split' not in ''.join(sys.argv):
                mylist = ''
                list_files = os.listdir(exp_folder)
                for each_file in list_files:
                    if '.mp4' in each_file.lower() or '.mov'in each_file.lower():
                            mylist += f"file '{pathjoin(exp_folder,  each_file)}'\n"
                with open (pathjoin(exp_folder,  'mylist.txt'), 'w', encoding='utf-8') as video_list_file:
                    video_list_file.write(mylist)
                final_code = F'ffmpeg -f concat -safe 0 -i "{pathjoin(exp_folder, "mylist.txt")}" -codec copy -y -map 0:v -map 0:a -map 0:s "{pathjoin(os.path.split(exp_folder)[0], file_name)}.mp4"'
                os.system(final_code)            
                print(final_code)


