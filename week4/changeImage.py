#!/usr/bin/env python3
import os
from PIL import Image

def convert_images(image_dir, size, output_format):
    for infile in os.listdir(image_dir):
        # Skip any non-TIFF files
        if not infile.endswith('.tiff'):
            continue

        # Convert image to desired format
        outfile = os.path.splitext(infile)[0]
        with Image.open(os.path.join(image_dir, infile)).convert('RGB') as im:
            im.thumbnail(size)
            output_path = os.path.join(image_dir, outfile + '.' + output_format)
            im.save(output_path, output_format.upper())
            print(f"Converted {infile} to {output_format} format.")

def main():
    size = (600, 400)
    image_dir = os.path.expanduser('~/supplier-data/images')
    output_format = 'jpeg'
    convert_images(image_dir, size, output_format)

if __name__ == '__main__':
    main()
