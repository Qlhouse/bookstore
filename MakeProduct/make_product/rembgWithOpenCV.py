from rembg.bg import remove
import numpy as np
import io
from PIL import ImageFile, Image

input_path = 'removeBackground.jpg'
output_path = 'afterRmBg2.png'

# img = cv2.imread(input_path)
# img_rembg = remove(img)
# # Convert PIL image to OpenCV image，想先存储再用opencv打开，但试了没影响
# img_cv2 = cv2.cvtColor(np.array(img_rembg), cv2.COLOR_RGBA2BGRA)
# cv2.imwrite('img_pil_opencv.png', img)


# # Remove background
# # Uncomment the following line if working with trucated image formats (ex. JPEG / JPG)
ImageFile.LOAD_TRUNCATED_IMAGES = True

# f = np.fromfile(input_path)
f = Image.open(input_path)
result = remove(f)
# img = Image.open(io.BytesIO(result)).convert("RGBA")
img = result.convert("RGBA")
img.save(output_path)

# # Convert PIL image to OpenCV image，想先存储再用opencv打开，但试了没影响
# img = cv2.cvtColor(np.array(img), cv2.COLOR_RGBA2BGRA)
# cv2.imwrite('img_pil_opencv.png', img)
