import os
import subprocess


class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

def cmd_code(code, keyword):
    cmd = f'{code}'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    for line in process.stdout:
        print(line)
        if keyword.lower() in line.lower() and keyword:
            return line.strip()

def detect_flash():
    cmd = f'{"wmic logicaldisk where drivetype=2 get"}'
    keyword = 'Removable Disk'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
    for line in process.stdout:
        line = line.strip()
        if keyword.lower() in line.lower() and keyword:
            flash_disc = line[line.find(keyword)+16]
            # print(type(flash_disc))
            return flash_disc
    
def format_detect(link):
    format_list = ['.mp4', '.mov', '.wav', '.mxf', '.avi', '.mkv', '.vob', '.ac3', '.m2ts', '.aac', '.flac', '.m4v', '.mpg', '.mp3', '.ts', '.m4a', '.m2t', '.avc', '.mts', '.mka']
    if link[link.rfind('.'):].lower() in format_list:
        return True
    else:
        return False
   
   
def dvd_collect(link):
    files = os.listdir(link)
    finput = []
    for vid in files:
        if format_detect(vid):
            name_list = []
            vts_size = 0
            vts_link = link+'\\'+vid
            if '1' in vid.split('_')[-1]: 
                for i in range(1, 10):
                    vts_name = f"{vts_link[:vts_link.rfind('_')]}_{i}.VOB"
                    if os.path.isfile(vts_name) and os.path.getsize(vts_name) > 10_000_000:
                        name_list.append(vts_name)
                        vts_size += os.path.getsize(vts_name)
            if vts_size > 500_000_000:
                finput.append(f"concat:{'|'.join(name_list)}")
    return(finput)

 


def extract_streams(link):
    info = ''
    info_dict = {}
    stream_info = []
    code_list = []
    if detect_flash():
        flsh_folder = f'{detect_flash()}:\\\\torrent/'
    else:
        flsh_folder = 'C:\\Yandex_Disc_Syn\\YandexDisk\\work files\\streams\\'
    # print(link)
    cmd = (f'ffprobe -hide_banner -v error -i "{link}" -show_streams ')
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True, encoding='utf-8')
    for line in process.stdout:
        info += line
        # print(line.strip())
    # info = info.split('[STREAM]')
    for stream in info.split('[STREAM]'):
        # print(stream)
        if 'codec_type=video' in stream and 'jpeg' not in stream:
            # print(stream)
            for line in stream.split():
                if "=" in line and 'r_frame_rate=' in line :
                    frame_rate = int(float(line.split('=')[1].split('/')[0]) / float(line.split('=')[1].split('/')[1]))
                    break
        elif 'codec_type=audio' in stream:
            for line in stream.split():
                if "=" in line:
                    info_dict[line.split("=")[0]] = line.split("=")[1]
            if info_dict:
                stream_info.append(info_dict.copy())
    for infoo in stream_info:
        lang_tag = infoo["TAG:language"] if "TAG:language" in infoo else ""
        # if 'BDMV' in link:
        #     name = link[:link.rfind('BDMV')-1]
        #     input(name)
        #     name = f'{link[link.rfind("/")+1:link[:link.rfind('BDMV')-1].rfind(".")].replace(".", "_").replace("(", "_").replace(")", "_")}_stream{infoo["index"]}_{lang_tag}_{infoo["channel_layout"].replace(".","")}_{frame_rate}fps_{infoo["codec_name"]}_TORRENT.wav'
        if '.VOB' in link:
            name = f"{''.join(filter(str.isalnum, link.split('\\')[2]))}_{(stream_info[0]['duration'])}"
        elif 'BDMV' in link:
            name = link[:link.rfind('BDMV')].strip('\\').strip('/').split('\\')[-1].split('/')[-1]
        else:
            name = link[link.rfind('\\'):].strip('\\')
            name = name[name.rfind("/")+1:name.rfind(".")]
        name = name.replace(".", "_").replace("(", "_").replace(")", "_").replace(" ", "_")
        name += f'_stream{infoo["index"]}_{lang_tag}_{infoo["channel_layout"].replace(".","")}_{frame_rate}fps_{infoo["codec_name"]}_TORRENT.wav'
        if 'truehd' in infoo["codec_name"] or 'pcm_bluray' in infoo["codec_name"]:
            codec = 'pcm_s24le'
        else:
            codec = 'copy'
        # print('name', name)
        if name not in os.listdir(flsh_folder) and int(infoo["channels"]) > 2:
            code_list.append( f'ffmpeg -loglevel warning -hide_banner -stats -i "{link}" -rf64 auto -codec {codec} -map 0:{infoo["index"]} -y "{flsh_folder}{name}"')
            # print(code_list)
        # input(name)
    return code_list

if __name__ == "__main__":
    yansyn = ''
    if not detect_flash():
        print('We need flash disc!')
        yansyn = input('copy to yandex disc syn? enter y: ')
    if detect_flash() or 'y' in yansyn:    
        os.system('nano torrent_folder.txt')
        with open ('torrent_folder.txt', 'r', encoding='utf-8') as tor_folder:
            tor_folder = tor_folder.readlines()
        for tor_link in tor_folder:
            tor_link = tor_link.strip() + '/'
            if 'BDMV' in tor_link:
                bd_link = ''
                bd_size = 0
                for bd_file in os.listdir(tor_link):
                    if os.path.getsize(tor_link+bd_file) > bd_size:
                        bd_link = bd_file
                        bd_size = os.path.getsize(tor_link+bd_file)
                code_list = extract_streams(f'{tor_link}{bd_link.strip()}')
                if code_list:
                    for code in code_list:
                        print(bcolors.HEADER, code, bcolors.ENDC)
                        os.system(code)

            elif 'VIDEO_TS' in tor_link:
                for dvd in dvd_collect(tor_link):
                    code_list = extract_streams(dvd)
                    if code_list:
                        for code in code_list:
                            print(bcolors.WARNING, code, bcolors.ENDC)
                            os.system(code)
                
            else:
                for file in os.listdir(tor_link):
                    if format_detect(file.strip()):
                        code_list = extract_streams(f'{tor_link}{file.strip()}')
                        if code_list:
                            for code in code_list:
                                print(bcolors.OKBLUE, code, bcolors.ENDC)
                                os.system(code)



'''
[STREAM]
    index=0
    codec_name=h264
    codec_long_name=H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
    profile=High
    codec_type=video
    codec_tag_string=avc1
    codec_tag=0x31637661
    width=1920
    height=1080
    coded_width=1920
    coded_height=1080
    closed_captions=0
    film_grain=0
    has_b_frames=1
    sample_aspect_ratio=1:1
    display_aspect_ratio=16:9
    pix_fmt=yuvj420p
    level=42
    color_range=pc
    color_space=unknown
    color_transfer=unknown
    color_primaries=unknown
    chroma_location=left
    field_order=progressive
    refs=1
    is_avc=true
    nal_length_size=4
    id=0x1
    r_frame_rate=50/1
    avg_frame_rate=50/1
    time_base=1/50000
    start_pts=0
    start_time=0.000000
    duration_ts=384000
    duration=7.680000
    bit_rate=51086847
    max_bit_rate=N/A
    bits_per_raw_sample=8
    nb_frames=384
    nb_read_frames=N/A
    nb_read_packets=N/A
    extradata_size=122
    DISPOSITION:default=1
    DISPOSITION:dub=0
    DISPOSITION:original=0
    DISPOSITION:comment=0
    DISPOSITION:lyrics=0
    DISPOSITION:karaoke=0
    DISPOSITION:forced=0
    DISPOSITION:hearing_impaired=0
    DISPOSITION:visual_impaired=0
    DISPOSITION:clean_effects=0
    DISPOSITION:attached_pic=0
    DISPOSITION:timed_thumbnails=0
    DISPOSITION:captions=0
    DISPOSITION:descriptions=0
    DISPOSITION:metadata=0
    DISPOSITION:dependent=0
    DISPOSITION:still_image=0
    TAG:creation_time=2024-10-20T11:16:04.000000Z
    TAG:language=und
    TAG:handler_name=Video Media Handler
    TAG:vendor_id=[0][0][0][0]
    TAG:encoder=AVC Coding
[/STREAM]
[STREAM]
    index=1
    codec_name=pcm_s16be
    codec_long_name=PCM signed 16-bit big-endian
    profile=unknown
    codec_type=audio
    codec_tag_string=twos
    codec_tag=0x736f7774
    sample_fmt=s16
    sample_rate=48000
    channels=2
    channel_layout=unknown
    bits_per_sample=16
    id=0x2
    r_frame_rate=0/0
    avg_frame_rate=0/0
    time_base=1/48000
    start_pts=0
    start_time=0.000000
    duration_ts=368640
    duration=7.680000
    bit_rate=1536000
    max_bit_rate=N/A
    bits_per_raw_sample=N/A
    nb_frames=368640
    nb_read_frames=N/A
    nb_read_packets=N/A
    DISPOSITION:default=1
    DISPOSITION:dub=0
    DISPOSITION:original=0
    DISPOSITION:comment=0
    DISPOSITION:lyrics=0
    DISPOSITION:karaoke=0
    DISPOSITION:forced=0
    DISPOSITION:hearing_impaired=0
    DISPOSITION:visual_impaired=0
    DISPOSITION:clean_effects=0
    DISPOSITION:attached_pic=0
    DISPOSITION:timed_thumbnails=0
    DISPOSITION:captions=0
    DISPOSITION:descriptions=0
    DISPOSITION:metadata=0
    DISPOSITION:dependent=0
    DISPOSITION:still_image=0
    TAG:creation_time=2024-10-20T11:16:04.000000Z
    TAG:language=und
    TAG:handler_name=Sound Media Handler
    TAG:vendor_id=[0][0][0][0]
[/STREAM]
[STREAM]
    index=2
    codec_name=unknown
    codec_long_name=unknown
    profile=unknown
    codec_type=data
    codec_tag_string=rtmd
    codec_tag=0x646d7472
    id=0x3
    r_frame_rate=0/0
    avg_frame_rate=0/0
    time_base=1/50000
    start_pts=0
    start_time=0.000000
    duration_ts=384000
    duration=7.680000
    bit_rate=409600
    max_bit_rate=N/A
    bits_per_raw_sample=N/A
    nb_frames=384
    nb_read_frames=N/A
    nb_read_packets=N/A
    DISPOSITION:default=1
    DISPOSITION:dub=0
    DISPOSITION:original=0
    DISPOSITION:comment=0
    DISPOSITION:lyrics=0
    DISPOSITION:karaoke=0
    DISPOSITION:forced=0
    DISPOSITION:hearing_impaired=0
    DISPOSITION:visual_impaired=0
    DISPOSITION:clean_effects=0
    DISPOSITION:attached_pic=0
    DISPOSITION:timed_thumbnails=0
    DISPOSITION:captions=0
    DISPOSITION:descriptions=0
    DISPOSITION:metadata=0
    DISPOSITION:dependent=0
    DISPOSITION:still_image=0
    TAG:creation_time=2024-10-20T11:16:04.000000Z
    TAG:language=und
    TAG:handler_name=Timed Metadata Media Handler
    TAG:timecode=09:22:26:48
[/STREAM]'''