import os
import shutil


os.system('nano concate_links.txt')
with open('concate_links.txt', 'r', encoding='utf-8') as link_file:
    for link in link_file:
        link = link.strip()
        print(link)
        if 'Convert' in  os.listdir('G:\WORK F\EXPORT_X'):
            shutil.rmtree('G:\WORK F\EXPORT_X/Convert')
            print('Dir "Convert" is delited')
        os.mkdir('G:\WORK F\EXPORT_X/Convert') 
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
        print(list_files)
        for each_file in list_files:
            if '.mp4'in each_file.lower() or '.mov' in each_file.lower() or '.braw' in each_file.lower():
                print('braw')
                video_list += f"file '{each_file}'\n"
                filters = "scale=1920:1080"
                if '.mp4' in each_file.lower():
                    filters += ", lut3d=A7s_Cine_Filipp_Bloom.cube"
                
                each_convert = f'ffmpeg -i "{link}/{each_file}" -c:a aac -rf64 auto -c:v h264 -profile:v baseline -preset ultrafast  -pix_fmt yuv420p -crf 25 -vf "{filters}" -y "G:\WORK F\EXPORT_X\Convert/{each_file[:each_file.find(".")]}.mp4"'
                print('each_convert', each_convert)
                os.system(each_convert)
        with open ('G:\WORK F\EXPORT_X\Convert/mylist.txt', 'w') as video_list_file:
            list_files = os.listdir ('G:\WORK F\EXPORT_X\Convert/')
            print(list_files)
            for each_file in list_files:
                if '.mp4'in each_file.lower() or '.mov'in each_file.lower():
                    video_list_file.write(f"file '{each_file}'\n")
        if 'EXPORT_E' not in os.listdir("E:\\"):
            os.mkdir('E:\\EXPORT_E')
        final_code = F'ffmpeg -f concat -safe 0 -i "G:\WORK F\EXPORT_X\Convert/mylist.txt" -codec copy -y "E:\\EXPORT_E\\{file_name}.mp4"'
        os.system("(for %i in (*.mp4) do @echo file '%i') > mylist.txt ")
        os.system(final_code)            
        print(final_code)
        print(list_files)   
print('G:\export_g/Convert/mylist.txt')

# for %i in (*.mp4) do ffmpeg -i %i -c:a aac -rf64 auto -c:v h264 -profile:v baseline -preset ultrafast  -pix_fmt yuv420p -crf 20 -vf scale=1920:1080,fps=25,lut3d="A7s_Cine_Filipp_Bloom.cube" -y "./EXPORT_X/%i"
# (for %i in (*.wav) do @echo file '%i') > mylist.txt
# ffmpeg -f concat -safe 0 -i "mylist.txt" -c:a aac -rf64 auto -c:v h264 -profile:v baseline -preset ultrafast  -pix_fmt yuv420p -crf 20 -vf scale=1920:1080,fps=25,lut3d="A7s_Cine_Filipp_Bloom.cube" -y "Export.mp4"

#ffmpeg -i "C5101.MP4" -c:a aac -rf64 auto -c:v h264 -profile:v baseline -preset ultrafast  -pix_fmt yuv420p -crf 20 -vf "scale=1920:1080,fps=25,lut3d=A7s_Cine_Filipp_Bloom.cube" -y "C5101_.MP4"
#,fps=25,lut3d=A7s_Cine_Filipp_Bloom.cube

