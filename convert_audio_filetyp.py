import argparse
from pydub import AudioSegment
import os

# Create argument parser
parser = argparse.ArgumentParser(description='Convert audio file formats.')
parser.add_argument('--input_file', type=str, required=True, help='Path to the input audio file')

# Parse arguments
args = parser.parse_args()

# Extract the file extension
file_extension = os.path.splitext(args.input_file)[1]

# Check the file extension and perform the conversion
if file_extension == ".mp3":
    # Load the mp3 file
    mp3_file = AudioSegment.from_mp3(args.input_file)
    # Export the mp3 file as wav
    output_file = os.path.splitext(args.input_file)[0] + '.wav'
    mp3_file.export(output_file, format="wav")
    print(f"Converted {args.input_file} to {output_file}")
elif file_extension == ".wav":
    # Load the wav file
    wav_file = AudioSegment.from_wav(args.input_file)
    # Export the wav file as mp3
    output_file = os.path.splitext(args.input_file)[0] + '.mp3'
    wav_file.export(output_file, format="mp3")
    print(f"Converted {args.input_file} to {output_file}")
else:
    print(f"Unsupported file format: {file_extension}")



