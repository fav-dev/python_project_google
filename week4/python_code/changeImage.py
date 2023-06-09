#!/usr/bin/env python3
import os
from PIL import Image

size = (600, 400)
image_dir = os.path.expanduser('~/supplier-data/images')
for infile in os.listdir(image_dir):
    # Skip any non-TIFF files
    if not infile.endswith('.tiff'):
        continue

    outfile = os.path.splitext(infile)[0]
    with Image.open(os.path.join(image_dir, infile)).convert('RGB') as im:
        im.thumbnail(size)
        im.save(os.path.join(image_dir, outfile + '.jpeg'), "JPEG")
        print(im.format)