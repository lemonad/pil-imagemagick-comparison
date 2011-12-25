# -*- coding: utf-8 -*-
"""
Generate image strips from the ./images directory for checking
cropping.

"""
import os
import re

from PIL import Image, ImageFilter, ImageOps
from subprocess import call


for dirname, dirnames, filenames in os.walk("./images"):
    for filename in filenames:
        path = os.path.join(dirname, filename)

        if re.search("\.(jpg|jpeg|gif|png|bmp)$", path):
            print filename
            output_filename = re.sub("\.(jpg|jpeg|gif|png|bmp)$", "", filename)
            output_path = os.path.join("./output", output_filename)
            h_path = output_path + "-hstrip.jpg"
            v_path = output_path + "-vstrip.jpg"

            im = Image.open(path)
            # ImageOps compatible mode
            if im.mode not in ("L", "RGB"):
                im = im.convert("RGB")

            imresize = im.resize((1000, 25), Image.ANTIALIAS)
            imresize.save(h_path, "JPEG", quality=90, optimize=True)

            imresize = im.resize((25, 1000), Image.ANTIALIAS)
            imresize.save(v_path, "JPEG", quality=90, optimize=True)
