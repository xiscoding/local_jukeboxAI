#use this as the launchpad for sample.py
import os
import datetime
#model to be used 
    #1b_lyrics, 5b, 5b_lyrics
MODEL = '1b_lyrics'
x = datetime.datetime.now()

#name of the project
NAME = f'sample_{MODEL}_{x.strftime("%b%d%f")}'

#number of model levels to use? no reason to not choose 3 
LEVELS = 3

#generate first sample_length_in_seconds seconds from total length total_sample_length_in_seconds
SAMPLE_LENGTH = 20
TOTAL_SAMPLE_LENGTH = 180

#sample rate (5.5 Samples, jukebox whitepaper)"improved fidelity by using 44khz"
SAMPLE_RATE = 44100

#number of samples to be generated at once
N_SAMPLES=6

#the length of jumps between samples
HOP_FRACTION='0.5,0.5,0.125'


os.system("cd ~/jukebox")

os.system(f"python jukebox/sample.py --model={MODEL}\
                                                          --name={NAME}\
                                                          --levels={LEVELS}\
                                                          --sample_length_in_seconds={SAMPLE_LENGTH}\
                                                          --total_sample_length_in_seconds={TOTAL_SAMPLE_LENGTH}\
                                                          --sr={SAMPLE_RATE}\
                                                          --n_samples={N_SAMPLES}\
                                                          --hop_fraction={HOP_FRACTION}\
                                                          ")