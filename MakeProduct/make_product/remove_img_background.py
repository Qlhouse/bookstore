from rembg.bg import remove
from PIL import ImageFile, Image


def rembg(image, truncated=False):

    # image: image data opened by pillow
    # # Remove background
    # # Uncomment the following line if working with trucated image formats (ex. JPEG / JPG)
    if truncated:
        ImageFile.LOAD_TRUNCATED_IMAGES = True

    return remove(image)


if __name__ == '__main__':
    input_path = 'removeBackground.jpg'
    output_path = 'afterRmBg2.png'

    image = Image.open(input_path)
    # img = Image.open(io.BytesIO(result)).convert("RGBA")
    img = rembg(image, True).convert("RGBA")
    img.save(output_path)
