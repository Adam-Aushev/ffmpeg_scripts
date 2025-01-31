import yt_dlp
import os
def download(link, name='%(title)s'):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', #берем самое лучшее качество видео и фото
        'outtmpl': '{}.%(ext)s'.format(name), #наше выбраное имя, если его не было, то стандартное - название видео на самом сайте
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        downloaded_file_path = ydl.prepare_filename(info_dict)
    print(f"Видео {downloaded_file_path} успешно загружено!")
    file_name = downloaded_file_path
    out_name = f"{file_name[:file_name.rfind('.')]}.mp3"
    convert = input('Press 1 to convert this file to mp3? ')
    if convert == '1':
        os.system(f'ffmpeg -v error -stats -i "{file_name}" -vn -codec mp3  "{out_name}"')
    return downloaded_file_path
os.system('nano youdowfile.txt')
with open ('youdowfile.txt', 'r', encoding='utf-8') as yolist:
    yolist = yolist.readlines()
    for ylink in yolist:
        print(download(ylink.strip()))