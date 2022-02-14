# Move downloaded images to "synopsisImgDir".
import shutil
import os
import argparse

parser = argparse.ArgumentParser(description="指定图片要移到的目录")
parser.add_argument("targetFold", type=str, help="指定图片要移到的目录")
args = parser.parse_args()
targetFold = args.targetFold

originalPath = r"C:\Users\xq127\Downloads\pictures\synopsisImgDir"
destinationPath = os.path.join(
    r"D:\bookStore\productData", targetFold, "synopsisImgDir"
)

# Remove original image in "detailImageDir"
for filename in os.listdir(destinationPath):
    file_path = os.path.join(destinationPath, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print("Failed to delete %s. Reason: %s" % (file_path, e))


for file in os.scandir(originalPath):
    # shutil.move(file.path, os.path.join(destinationPath, file.name))
    shutil.move(file.path, destinationPath)

# remove images in originalPath
# for filename in os.listdir(originalPath):
#     file_path = os.path.join(originalPath, filename)
#     try:
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         print("Failed to delete %s. Reason: %s" % (file_path, e))
