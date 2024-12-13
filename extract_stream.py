import os
import subprocess



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
'''[STREAM]
index=0
codec_name=h264
codec_long_name=H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
profile=High
codec_type=video
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
width=1920
height=816
coded_width=1920
coded_height=816
closed_captions=0
film_grain=0
has_b_frames=2
sample_aspect_ratio=1:1
display_aspect_ratio=40:17
pix_fmt=yuv420p
level=41
color_range=tv
color_space=bt709
color_transfer=bt709
color_primaries=bt709
chroma_location=left
field_order=progressive
refs=1
is_avc=true
nal_length_size=4
id=N/A
r_frame_rate=24/1
avg_frame_rate=24/1
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=N/A
duration=N/A
bit_rate=N/A
max_bit_rate=N/A
bits_per_raw_sample=8
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
extradata_size=45
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
TAG:BPS=14571578
TAG:DURATION=02:16:05.667000000
TAG:NUMBER_OF_FRAMES=195976
TAG:NUMBER_OF_BYTES=14873332293
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=1
codec_name=ac3
codec_long_name=ATSC A/52A (AC-3)
profile=unknown
codec_type=audio
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
sample_fmt=fltp
sample_rate=48000
channels=6
channel_layout=5.1(side)
bits_per_sample=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=N/A
duration=N/A
bit_rate=448000
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
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
TAG:language=rus
TAG:title=Dub
TAG:BPS=448000
TAG:DURATION=02:16:03.776000000
TAG:NUMBER_OF_FRAMES=255118
TAG:NUMBER_OF_BYTES=457171456
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=2
codec_name=eac3
codec_long_name=ATSC A/52B (AC-3, E-AC-3)
profile=unknown
codec_type=audio
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
sample_fmt=fltp
sample_rate=48000
channels=2
channel_layout=stereo
bits_per_sample=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=N/A
duration=N/A
bit_rate=192000
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
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
TAG:language=rus
TAG:title=MVO - Time Media Group
TAG:BPS=192000
TAG:DURATION=02:16:04.512000000
TAG:NUMBER_OF_FRAMES=255141
TAG:NUMBER_OF_BYTES=195948288
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=3
codec_name=dts
codec_long_name=DCA (DTS Coherent Acoustics)
profile=DTS
codec_type=audio
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
sample_fmt=fltp
sample_rate=48000
channels=6
channel_layout=5.1(side)
bits_per_sample=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=N/A
duration=N/A
bit_rate=1536000
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
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
TAG:language=rus
TAG:title=DVO - BBC Saint-Petersburg
TAG:BPS=1509000
TAG:DURATION=02:16:05.664000000
TAG:NUMBER_OF_FRAMES=765531
TAG:NUMBER_OF_BYTES=1540248372
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=4
codec_name=eac3
codec_long_name=ATSC A/52B (AC-3, E-AC-3)
profile=unknown
codec_type=audio
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
sample_fmt=fltp
sample_rate=48000
channels=8
channel_layout=7.1
bits_per_sample=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=N/A
duration=N/A
bit_rate=1536000
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
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
TAG:language=chi
TAG:title=Chinese
TAG:BPS=1536000
TAG:DURATION=02:16:05.664000000
TAG:NUMBER_OF_FRAMES=255177
TAG:NUMBER_OF_BYTES=1567807488
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=5
codec_name=subrip
codec_long_name=SubRip subtitle
profile=unknown
codec_type=subtitle
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
width=N/A
height=N/A
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=8165667
duration=8165.667000
bit_rate=N/A
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
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
TAG:language=rus
TAG:title=Russian
TAG:BPS=60
TAG:DURATION=02:07:55.937000000
TAG:NUMBER_OF_FRAMES=1332
TAG:NUMBER_OF_BYTES=58400
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=6
codec_name=subrip
codec_long_name=SubRip subtitle
profile=unknown
codec_type=subtitle
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
width=N/A
height=N/A
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=8165667
duration=8165.667000
bit_rate=N/A
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
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
TAG:language=eng
TAG:title=English
TAG:BPS=40
TAG:DURATION=02:07:56.791000000
TAG:NUMBER_OF_FRAMES=1690
TAG:NUMBER_OF_BYTES=38644
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=7
codec_name=subrip
codec_long_name=SubRip subtitle
profile=unknown
codec_type=subtitle
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
width=N/A
height=N/A
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/1000
start_pts=0
start_time=0.000000
duration_ts=8165667
duration=8165.667000
bit_rate=N/A
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
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
TAG:language=chi
TAG:title=Chinese
TAG:BPS=41
TAG:DURATION=02:06:13.610000000
TAG:NUMBER_OF_FRAMES=1674
TAG:NUMBER_OF_BYTES=39605
TAG:_STATISTICS_WRITING_APP=mkvmerge v73.0.0 ('25 or 6 to 4') 64-bit
TAG:_STATISTICS_WRITING_DATE_UTC=2023-02-05 10:31:16
TAG:_STATISTICS_TAGS=BPS DURATION NUMBER_OF_FRAMES NUMBER_OF_BYTES
[/STREAM]
[STREAM]
index=8
codec_name=mjpeg
codec_long_name=Motion JPEG
profile=Baseline
codec_type=video
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
width=500
height=750
coded_width=500
coded_height=750
closed_captions=0
film_grain=0
has_b_frames=0
sample_aspect_ratio=1:1
display_aspect_ratio=2:3
pix_fmt=yuvj420p
level=-99
color_range=pc
color_space=bt470bg
color_transfer=unknown
color_primaries=unknown
chroma_location=center
field_order=unknown
refs=1
id=N/A
r_frame_rate=90000/1
avg_frame_rate=0/0
time_base=1/90000
start_pts=0
start_time=0.000000
duration_ts=734910030
duration=8165.667000
bit_rate=N/A
max_bit_rate=N/A
bits_per_raw_sample=8
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
DISPOSITION:dub=0
DISPOSITION:original=0
DISPOSITION:comment=0
DISPOSITION:lyrics=0
DISPOSITION:karaoke=0
DISPOSITION:forced=0
DISPOSITION:hearing_impaired=0
DISPOSITION:visual_impaired=0
DISPOSITION:clean_effects=0
DISPOSITION:attached_pic=1
DISPOSITION:timed_thumbnails=0
DISPOSITION:captions=0
DISPOSITION:descriptions=0
DISPOSITION:metadata=0
DISPOSITION:dependent=0
DISPOSITION:still_image=0
TAG:filename=cover.jpg
TAG:mimetype=image/jpeg
[/STREAM]

F:\torrent>'''
def extract_streams(link):
    info = ''
    info_dict = {}
    stream_info = []
    flsh_folder = f'{detect_flash()}:\\\\torrent/'
    print(link)
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
        print(link[:link.rfind("BDMV")-1])
        name = link[:link.rfind('BDMV')].strip('\\')
        name = name[name.rfind('\\'):].strip('\\')
        name = name[name.rfind("/")+1:name.rfind(".")].replace(".", "_").replace("(", "_").replace(")", "_").replace(" ", "_")
        name += f'_stream{infoo["index"]}_{lang_tag}_{infoo["channel_layout"].replace(".","")}_{frame_rate}fps_{infoo["codec_name"]}_TORRENT.wav'
        if 'truehd' in infoo["codec_name"]:
            codec = 'pcm_s24le'
        else:
            codec = 'copy'
        print(name in os.listdir(flsh_folder))
        if name not in os.listdir(flsh_folder):
            code = f'ffmpeg   -i "{link}" -rf64 auto -codec {codec} -map 0:{infoo["index"]} -y "{flsh_folder}{name}"'
            print(code)
            return code

if __name__ == "__main__":
    if not detect_flash():
        print('We need flash disc!')
    else:    
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
                os.system(extract_streams(f'{tor_link}{bd_link.strip()}'))
            else:
                for file in os.listdir(tor_link):
                    if format_detect(file.strip()):
                        os.system(extract_streams(f'{tor_link}{file.strip()}'))