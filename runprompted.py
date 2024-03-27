#use this as the launchpad for sample.py
import os
import datetime
from file_selector import FileSelectionDialog

INITIAL_DIR='/home/xdoestech/audio_center/audio_samples/'

#model to be used 
    #1b_lyrics, 5b, 5b_lyrics
MODEL = '5b_lyrics'

x = datetime.datetime.now()

#name of the project
NAME = f'prompted_{MODEL}_{x.strftime("%b%d%f")}'

#number of model levels to use? no reason to not choose 3 
LEVELS = 3

MODE = 'primed'

dialog = FileSelectionDialog()
selections = dialog.get_file_names_string()
AUDIO_IN = f'{selections}'
print(AUDIO_IN)

# prompt_length_in_seconds
PROMPT_LENGTH = 24

#generate first sample_length_in_seconds seconds from total length total_sample_length_in_seconds
SAMPLE_LENGTH = 48

TOTAL_SAMPLE_LENGTH = 360

#sample rate (5.5 Samples, jukebox whitepaper)"improved fidelity by using 44khz"
SAMPLE_RATE = 44100

#number of samples to be generated at once
N_SAMPLES=3

#the length of jumps between samples
HOP_FRACTION='0.5,0.5,0.125'

PATH_TO_SAMPLYPY='/home/xdoestech/audio_center/ai/jukebox/jukebox/sample.py'

os.system(f"python {PATH_TO_SAMPLYPY} --model={MODEL}\
                                                          --name={NAME}\
                                                          --levels={LEVELS}\
                                                          --mode={MODE}\
                                                          --audio_file={AUDIO_IN}\
                                                          --prompt_length_in_seconds={PROMPT_LENGTH}\
                                                          --sample_length_in_seconds={SAMPLE_LENGTH}\
                                                          --total_sample_length_in_seconds={TOTAL_SAMPLE_LENGTH}\
                                                          --sr={SAMPLE_RATE}\
                                                          --n_samples={N_SAMPLES}\
                                                          --hop_fraction={HOP_FRACTION}\
                                                          ")