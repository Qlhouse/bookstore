import time
import os
import numpy as np

# from PIL import Image
import cv2
import requests
import queue
from bs4 import BeautifulSoup
import argparse
from selenium import webdriver
import shutil

parser = argparse.ArgumentParser(description="Product URL and xpath selector")
parser.add_argument("url", type=str, help="URL link to product")
parser.add_argument("fold", type=str, help="Product ID directory")
args = parser.parse_args()

url = args.url
fold = args.fold

imgStoredRootDir = r"D:\bookStore\productData"
outFileName = os.path.join(
    imgStoredRootDir, fold, "detailImageDir", "concatenatedDetail.jpg"
)

# Remove original image in "detailImageDir"
detailImageDir = os.path.join(imgStoredRootDir, fold, "detailImageDir")
for filename in os.listdir(detailImageDir):
    file_path = os.path.join(detailImageDir, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print("Failed to delete %s. Reason: %s" % (file_path, e))

# Scrape the product url, return a queue contains image urls
def getProductDetailImageUrls(url):
    driverPath = r"C:\Users\xq127\AppData\Local\seleniumDriver\geckodriver.exe"
    driver = webdriver.Firefox(executable_path=driverPath)
    driver.implicitly_wait(30)

    driver.get(url)

    # Scroll down to end of the page
    # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # SCROLL_PAUSE_TIME = 0.5
    #
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    #
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height

    time.sleep(5)
    driver.refresh()

    try:
        imgUrlQueue = queue.Queue()
        # Parse product detail image address
        # 获取内容简介节点
        productDetailTag = driver.find_element_by_xpath('//*[@id="description"]/div[2]')
        try:
            productDetailTag.find_element_by_tag("src")
        except:
            productDetailTag = driver.find_element_by_xpath('//*[@id="content"]/div[2]')
        # //*[@id="content"]/div[2]
        soup = BeautifulSoup(productDetailTag.get_attribute("innerHTML"), "html.parser")
        imgTag = soup.find("img")
        imgUrlQueue.put(imgTag["src"])
        while imgTag.next_sibling:
            imgTag = imgTag.next_sibling
            imgUrlQueue.put(imgTag["src"])

        return imgUrlQueue
        # while not imgUrlQueue.empty():
        #     print(imgUrlQueue.get())
    except:
        print("Sorry! 请重运行...")
    finally:
        # Close Firefox
        driver.quit()


# Download images in queue, concatenate them, write out
imgUrlQueue = getProductDetailImageUrls(url)

# openCV version
def downloadImageAndStoredInList(imgUrlQueue):
    imgList = []
    while not imgUrlQueue.empty():
        imgUrl = imgUrlQueue.get()
        if imgUrl.endswith(".jpg"):
            resp = requests.get(imgUrl, stream=True).raw
            img = np.asarray(bytearray(resp.read()), dtype=np.uint8)
            imgList.append(cv2.imdecode(img, -1))

    return imgList


# concatenate imgs
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [
        cv2.resize(
            im,
            (w_min, int(im.shape[0] * w_min / im.shape[1])),
            interpolation=interpolation,
        )
        for im in im_list
    ]
    return cv2.vconcat(im_list_resize)


imgList = downloadImageAndStoredInList(imgUrlQueue)

im_v_resize = vconcat_resize_min(imgList)
# print(outFileName)
cv2.imwrite(outFileName, im_v_resize)

print("Done...")

# pillow version
# def downloadImageAndStoredInList(imgUrlQueue):
#     imgList = []
#     while not imgUrlQueue.empty():
#         imgUrl = imgUrlQueue.get()
#         if imgUrl.endswith('.jpg'):
#             img = Image.open(requests.get(imgUrl, stream=True).raw)
#             imgList.append(img)
#
#     return imgList
#
# imgList = downloadImageAndStoredInList(imgUrlQueue)
# min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgList])[0][1]
# imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgList ))
# imgs_comb = Image.fromarray( imgs_comb)
# imgs_comb.save( 'Trifecta_vertical.jpg' )
