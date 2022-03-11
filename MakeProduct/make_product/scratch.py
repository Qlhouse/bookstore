from PIL import ImageFile, Image
from rembgV2 import rembg


input_path = 'removeBackground.jpg'
output_path = 'afterRmBg2.png'

image = Image.open(input_path)
# img = Image.open(io.BytesIO(result)).convert("RGBA")
img = rembg(image, True).convert("RGBA")
img.save(output_path)
