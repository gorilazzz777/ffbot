import uuid

from PIL import Image

def merge_images(path_1, path_2):
    img = Image.open(path_1)
    img1 = Image.open(path_2)
    width = img.width if img.width > img1.width else img1.width

    img2 = Image.new("RGB", (img.height + img1.height, width), "white")

    img2.paste(img, (0, 0))

    img2.paste(img1, (img.width, 0))
    path = f'trumb_img/{uuid.uuid4().hex}.jpg'
    img2.save(path)
    return path