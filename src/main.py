import os
import argparse
from readImage import read

parser = argparse.ArgumentParser()
parser.add_argument('--imgfile', type=str, default='training1.png')
args = parser.parse_args()

folder = os.path.join('..', 'data', 'train')
image_file = os.path.join(folder, args.imgfile)

# Read image
spanish_text = read(image_file)
print(spanish_text)

# Translate text
# todo

# Summarize text
     