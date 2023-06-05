#!/usr/bin/env python3
import os
import sys
from PIL import Image

size = (128, 128)
for infile in os.listdir('images'):
  if infile == '.DS_Store':
    continue
  outfile = os.path.splitext(infile)[0]
  with Image.open(os.path.join('images', infile)).convert('RGB') as im:
    im.thumbnail(size)
    im.rotate(270).save(outfile, "JPEG")
    print(im.format)
