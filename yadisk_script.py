import yadisk
import os
from concate import convert_video, get_compare
from dotenv import load_dotenv
import sys
load_dotenv() 


def chek_exp():
    dow_dir = 'downloads'
    exp_dir = 'export'
    dow_list = os.listdir(dow_dir)
    exp_list = os.listdir(exp_dir)
    exp_list = [os.path.splitext(each)[0] for each in exp_list ]
    for each in dow_list:
        src_path = os.path.join(dow_dir, each)
        exp_path = os.path.join(exp_dir, f'{os.path.splitext(each)[0]}.mp4')
        if os.path.splitext(each)[0] not in exp_list:
            print(os.path.splitext(each)[0])
            addlut = True if 'lut' in ''.join(sys.argv) else False
            code = convert_video(src_path, exp_path, codec='h265', lut=addlut)
            os.system(code)
        print(get_compare(src_path, exp_path))

        
def video_detect(link):
    format_list = ['.mp4', '.mov', '.wav', '.mxf', '.avi', '.mkv', '.vob', '.ac3', '.m2ts', '.aac', '.flac', '.m4v', '.mpg', '.mp3', '.ts', '.m4a', '.m2t', '.avc', '.mts', '.mka']
    if link[link.rfind('.'):].lower() in format_list:
        return True
    else:
        return False



if __name__ == "__main__":
    token = os.getenv('token')
    disk = yadisk.Client(token=token)
    # print(disk.listdir('/Банк/ЛЮБА/КУШТ.mp4'))
    with disk:
        # Проверяет, валиден ли токен
        dow_dir = 'downloads'
        exp_dir = 'export'
        dow_list = os.listdir(dow_dir)
        os.mkdir(dow_dir) if not os.path.isdir(dow_dir) else 1
        os.mkdir(exp_dir) if not os.path.isdir(exp_dir) else 1
        path = '/СВАДЬБЫ/СВОИ/АХМАД/ВИДЕО'
        files = disk.listdir(path)
        for each in files:
            each = each['name']
            dow_file = os.path.join(dow_dir, each)
            exp_file = os.path.join(exp_dir, f'{os.path.splitext(each)[0]}.mp4')
            if video_detect(each) and each not in dow_list:
                sys.stdout.write(f'{each} Download...\r')
                disk.download(os.path.join(path, each), dow_file)
                addlut = True if 'lut' in ''.join(sys.argv) else False
                code = convert_video(dow_file, exp_file, codec='h265', lut=addlut)
                os.system(code)
                print(get_compare(dow_file, exp_file))
        # disk.download('/Банк/ЛЮБА/КЛИПИК.mp4', 'КЛИПИК.mp4')
    chek_exp()



