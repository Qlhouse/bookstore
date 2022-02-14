from rembg.bg import remove
import numpy as np
import io
from PIL import Image

input_path = r'C:\Users\xq127\Desktop\Woman-Running-Sample-Image.jpg'
output_path = r'C:\Users\xq127\Desktop\output.jpg'

f = np.fromfile(input_path)
result = remove(f)
img = Image.open(io.BytesIO(result)).convert('RGBA')
img.save(output_path)