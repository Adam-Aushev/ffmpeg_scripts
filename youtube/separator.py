from audio_separator.separator import Separator
import os
import time
music_list = []
path = 'F:\Work E\музыка\музыка 2'
out_path = 'F:\Work E\музыка\Вокал Инструментал'
out_files = os.listdir(out_path)
for file in os.listdir(path):
    if '.mp3' in file and os.path.splitext(file)[0] not in ''.join(out_files):
        music_list.append(os.path.join(path,file))
# Initialize the Separator class (with optional configuration properties, below)
models = ['vocals_mel_band_roformer.ckpt', 'melband_roformer_big_beta4.ckpt', 'mel_band_roformer_kim_ft_unwa.ckpt', 'melband_roformer_big_beta5e.ckpt', 'MelBandRoformerBigSYHFTV1.ckpt']
separator = Separator()
separator.output_dir = out_path
# Load a model

separator.load_model(model_filename=models[0])
# Separate multiple audio files without reloading the model
output_files = separator.separate(music_list)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Model Filename                             Arch  Output Stems (SDR)                   Friendly Name
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# model_bs_roformer_ep_317_sdr_12.9755.ckpt  MDXC  vocals* (12.9), instrumental (17.0)  Roformer Model: BS-Roformer-Viperx-1297
# model_bs_roformer_ep_368_sdr_12.9628.ckpt  MDXC  vocals* (12.9), instrumental (17.0)  Roformer Model: BS-Roformer-Viperx-1296
# vocals_mel_band_roformer.ckpt              MDXC  vocals* (12.6), other                Roformer Model: MelBand Roformer | Vocals by Kimberley Jensen
# melband_roformer_big_beta4.ckpt            MDXC  vocals* (12.5), other                Roformer Model: MelBand Roformer Kim | Big Beta 4 FT by unwa
# mel_band_roformer_kim_ft_unwa.ckpt         MDXC  vocals* (12.4), other                Roformer Model: MelBand Roformer Kim | FT by unwa