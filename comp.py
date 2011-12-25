# -*- coding: utf-8 -*-
"""
Resizes images in the ./images directory with both PIL and ImageMagick.
The result is placed into the ./output directory.

"""
import os
import re

from PIL import Image, ImageFilter, ImageOps
from subprocess import call


sizes = [100, 50, 25]

for dirname, dirnames, filenames in os.walk("./images"):
    for filename in filenames:
        path = os.path.join(dirname, filename)

        if re.search("\.(jpg|jpeg|gif|png|bmp)$", path):
            print filename
            for size in sizes:
                output_filename = re.sub("\.(jpg|jpeg|gif|png|bmp)$",
                                         "",
                                         filename)
                output_path = os.path.join("./output", output_filename)
                im_path = output_path + "-%d-im.jpg" % size
                pil_path = output_path + "-%d-pil.jpg" % size

                im = Image.open(path)
                # ImageOps compatible mode
                if im.mode not in ("L", "RGB"):
                    im = im.convert("RGB")

                im.resize((100, 10), Image.ANTIALIAS)

                imops = ImageOps.fit(im, (size, size), Image.ANTIALIAS)
                imops.save(pil_path, "JPEG", quality=90, optimize=True)

                im_cmd = ["convert",
                          "%s" % path,
                          "-thumbnail", "%dx%d^" % (size, size),
                          "-gravity", "center",
                          "-quality", "90",
                          "-extent", "%dx%d" % (size, size),
                          "%s" % im_path]
                call(im_cmd)
