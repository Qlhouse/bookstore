import os
from selenium.webdriver.common.by import By
import json
from uploadProduct import uploadProduct, loginWeb, driver
from datetime import datetime
import logging
import time
from moveSuccessFold import moveSuccessedDirClearRecord

productData = r"D:\bookStore\productData"

logging.basicConfig(
    filename="failure.txt",
    filemode="w",
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

# 转走上传成功的文件夹，清空uploadSuccess.txt
moveSuccessedDirClearRecord()

# 登录网站账户和密码
certificateFile = "certification.json"
with open(certificateFile, "r", encoding="utf-8") as userInfo:
    certification = json.load(userInfo)

loginWeb(certification)

with os.scandir(productData) as productGenerator:
    direntries = list(productGenerator)  # reads all of the directory entries

direntries.sort(key=os.path.getctime)

# for entry in os.scandir(productData):
for entry in direntries:
    try:
        if entry.is_dir():
            uploadProduct(entry.path)
            time.sleep(2)
    except Exception as e:
        logging.exception(f"Upload {os.path.basename(entry.path)} failed")
        # linkToProductPage = driver.find_element(By.PARTIAL_LINK_TEXT, "商品")
        # linkToProductPage.click()
        driver.get(certification["redirection"])
        time.sleep(2)
    # finally:
    #     #     driver.close()
    #     for dirpath in dirList:
    #         try:
    #             shutil.move(entry.path, productBackupDir)
    #         except Exception as e:
    #             logging.exception(f"Move {os.path.basename(entry.path)} failed")

driver.close()
