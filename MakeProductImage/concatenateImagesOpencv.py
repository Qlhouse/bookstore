from imageProcessOpenCV import cropImage
import requests
import cv2
import os
import numpy as np
from pathlib import Path

def cropImages(directory, boundaries):
    miny, maxy, minx, maxx = boundaries
    for dirpath, dirnames, filenames in os.walk(directory):
        id = 1
        for baseName in filenames:
            file = Path(dirpath) / baseName
            img = cv2.imread(str(file))

            imgCroped = img[miny:maxy, minx:maxx]

            outputFileName = str(id) + '.png'
            outputFile = Path(dirpath) / outputFileName
            cv2.imwrite(str(outputFile), imgCroped) 
            id += 1

def concatenateImage(directory):
    img2 = cv2.imread(str(Path(directory) / '2.png'))

    img3 = cv2.imread(str(Path(directory) / '3.png'))

    img4 = cv2.imread(str(Path(directory) / '4.png'))

    img1 = cv2.imread(str(Path(directory) / '1.png'))

    bookletConcatenate = cv2.vconcat([img2, img3, img4])

    imgList = (img1, bookletConcatenate)
    heightMin = min(img.shape[0] for img in imgList)
    imgListResize = [cv2.resize(im, (int(im.shape[1] * heightMin / im.shape[0]), heightMin), 
                     interpolation=cv2.cv2.INTER_AREA) for im in imgList]

    concatenateImg = cv2.hconcat(imgListResize)

    outputBasename = Path(directory) / 'concatenation.png'
    cv2.imwrite(str(outputBasename), concatenateImg)

    files = {'smfile': open(outputBasename, 'rb')}
    uploadImages(files)



def uploadImages(files):
    api_addr = 'https://sm.ms/api/v2'
    upload_api = '/upload'
    url = api_addr + upload_api
    headers = {'Authorization': '5NUSX0M5dr3ewDHK5x8cqpfCCMHfB6e4'}

    resp = requests.post(url, files=files, headers=headers, verify=False).json()
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
    
directory = r'C:\Users\xq127\Pictures\concatenateImages'
boundaries = (500, 2040, 0, 1080)
# cropImages(directory, boundaries)
cropImages(directory, boundaries)
concatenateImage(directory)
