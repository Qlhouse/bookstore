from PIL import ImageFile, Image
from remove_img_background import rembg


input_path = 'removeBackground.jpg'
output_path = 'afterRmBg2.png'

image = Image.open(input_path)
# img = Image.open(io.BytesIO(result)).convert("RGBA")
img = rembg(image, True).convert("RGBA")
img.save(output_path)
