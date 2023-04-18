import os
import argparse
from readImage import read
from translateText import translate
from summarizeText import summarize

parser = argparse.ArgumentParser()
parser.add_argument('--imgfile', type=str, default='training1.png')
args = parser.parse_args()

folder = os.path.join('..', 'data', 'train')
image_file = os.path.join(folder, args.imgfile)

# Read image
spanish_text = read(image_file)
print(f"[Extract Spanish text from Image]:\n {spanish_text}")

# Translate text
english_text = translate(spanish_text)
print(f"[Translate Spanish to English]:\n {english_text}")

# Summarize text
summary = summarize(english_text)
print(f"[Summarize English text]:\n {summary}")
