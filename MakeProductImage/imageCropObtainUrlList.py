from PIL import Image, ImageEnhance
import os
from pathlib import Path
import requests
import time
from requests.sessions import session
from renameFilesInDirectory import renameFiles


'''
def cropImage(imageAddress, left, top, right, bottom):
    # Open a image in RGB mode
    # In Windows, address should be raw text
    im = Image.open(imageAddress)

    # Croped image of above dimension
    # It will not change original image
    im1 = im.crop((left, top, right, bottom))

    # Show the image in image viewer
    # imageOutputAddress = 'outputAddress'
    im1.save(imageAddress, quality=95)

    # Sharp image
    ehancer = ImageEnhance.Sharpness(im1)
    factor = 1.5
    im1 = ehancer.enhance(factor)
    im1.save(imageAddress, quality=95)
'''

# Traverse image files in a directory, crop files
def cropImagesInDirectory(directory, left, top, right, bottom):
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file = Path(dirpath) / file

            # Open a image in RGB mode
            im = Image.open(file)

            # Croped image accord to the given dimension
            # It will not change original image
            im1 = im.crop((left, top, right, bottom))

            # Resize image
            if im1.height > 1200:
                factor = 1200 / im1.height

            resizedImage = im1.resize((int(im1.width * factor), int(im1.height * factor)))

            # Sharp image
            ehancer = ImageEnhance.Sharpness(resizedImage)
            factor = 1.5
            outputImage = ehancer.enhance(factor)
            outputImage.save(file, quality=95)

            # cropImage(file)

# Upload image file to sm.ms(https://sm.ms/)
def uploadImages(directory):
    api_addr = 'https://sm.ms/api/v2'
    upload_api = '/upload'
    url = api_addr + upload_api
    headers = {'Authorization': '5NUSX0M5dr3ewDHK5x8cqpfCCMHfB6e4'}
    session = requests.Session()

    # In windows, directory should be in raw text, r'C:\Users\xq127\Pictures\temp'
    for dirpath, dirnames, filenames in os.walk(directory):
        urlStoredFileName = time.strftime(
            "%Y%m%d%H%M%S", time.localtime()) + '.txt'
        urlStoredFilePath = Path(dirpath) / urlStoredFileName

        for file in filenames:
            # upload image file
            file = Path(dirpath) / file
            files = {'smfile': open(file, 'rb')}
            # resp = session.post(
            #     url, files=files, headers=headers, verify=False).json()

            resp = session.post(url, files=files, headers=headers, verify=False).json()
            # print(json.dumps(resp, indent=4))

            # get image url
            code = resp.get('code')
            print(code)
            if code == 'image_repeated':
                imageUrl = resp.get("images")
            elif code == 'success':
                imageUrl = resp["data"]["url"]
            else:
                raise ValueError("API Error")
            print(imageUrl)

            with open(urlStoredFilePath, 'a') as fh:
                fh.write(imageUrl)
                fh.write('\n')


# path = Path(r'C:\Users\xq127\Pictures\temp\Screenshot_20210820_003926.jpg')
# url = uploadImage(path)
directory = r'C:\Users\xq127\Pictures\uploadImage'
coordinate = (0, 745, 1070, 2140)

renameFiles(directory)

cropImagesInDirectory(directory, *coordinate)

# uploadImages(directory)
# cropFileInTurn(r'C:\Users\xq127\Pictures\temp')
