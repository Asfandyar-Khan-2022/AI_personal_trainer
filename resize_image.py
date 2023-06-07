"""Resize image

Module to resize images in a folder by its width

Typical usage example:

    resize(folder directory, integer pixel width)
"""

from PIL import Image
import os


def resize(dir, new_width):
    """Changes image width with a fixed ratio

    Args:
        dir: Directory of folder containing images.
        new_width: New pixel width of the images.

    Raises:
        FileNotFoundError: If file path is not specified.
    """
    files = os.listdir(dir)
    extentions = ['jpg', 'jped', 'png', 'gif']

    for file in files:
        ext = file.split('.')[-1]

        if ext in extentions:
            im = Image.open(dir+'/'+file)
            width, height = im.size
            ratio = height/width
            new_height = int(ratio*new_width)
            im_resized = im.resize((new_width, new_height))
            filepath = f'{dir}/{file}'
            im_resized.save(filepath)

