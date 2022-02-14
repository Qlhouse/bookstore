import time
import os
import json
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driverPath = r"C:\Users\xq127\AppData\Local\seleniumDriver\geckodriver.exe"
# driverPath = r"C:\Users\xq127\AppData\Local\seleniumDriver\chromedriver.exe"
# driver = webdriver.Firefox(executable_path=driverPath, options=options)
driver = webdriver.Firefox(executable_path=driverPath)

# driver = webdriver.Firefox()


def loginWeb(certification):
    # Login to website
    driver.get(certification["targetWebsite"])
    usernameElement = driver.find_element_by_name("username")
    passwordElement = driver.find_element_by_name("password")
    usernameElement.send_keys(certification["username"])
    passwordElement.send_keys(certification["password"])

    driver.find_element_by_name("submit").click()
    time.sleep(5)


def uploadProduct(rootDir):
    # rootDir = os.path.dirname(os.path.realpath(__file__))
    # print(rootDir)

    # 要填充的文字资料
    productData = rootDir + "\\productDetail.json"
    with open(productData, "r", encoding="utf-8") as product:
        data = json.load(product)

    # # 登录网站账户和密码
    # certificateFile = rootDir + "\\certification.json"
    # with open(certificateFile, "r", encoding="utf-8") as userInfo:
    #     certification = json.load(userInfo)

    # 跳转到商品页
    linkToProductPage = driver.find_element_by_partial_link_text("商品")
    linkToProductPage.click()
    time.sleep(7)

    # 选择 "快速添加商品"
    addNewProductPage = driver.find_element_by_partial_link_text("快速添加商品")
    addNewProductPage.click()
    time.sleep(7)

    # Fill product information
    # 填写商品名称
    productNameElement = driver.find_element_by_id("goodsname")
    productNameElement.send_keys(data["商品名称"])
    # productNameElement.send_keys(Keys.ENTER)
    productNameElement.submit()

    # 填写单位
    productUnitElement = driver.find_element_by_id("unit")
    productUnitElement.send_keys(data["单位"])
    # productUnitElement.send_keys(Keys.ENTER)
    productUnitElement.submit()

    # 填写商品关键字， 用于搜索
    productKeyWord = driver.find_element_by_name("keywords")
    productKeyWord.send_keys(data["关键字"])
    productKeyWord.submit()

    # 填写商品分类
    # Pop up classification options
    popUpElement = driver.find_element_by_id("s2id_autogen1")
    popUpElement.click()
    # popUpElement.send_keys(Keys.ENTER)
    time.sleep(5)

    # The classification options is formed by ul list
    # Locate the choosed classification
    selectedClassification = data["商品分类"]
    classifyOptions = driver.find_element_by_xpath(
        f"//div[text()='{selectedClassification}']"
        # f"//*[@id='select2-result-label-41']/text()='{selectedClassification}']"
        # //*[@id="select2-result-label-121"]
        # //*[@id="select2-result-label-121"]/text()
    )
    classifyOptions.click()
    time.sleep(5)

    # 上传商品简介图片
    def uploadBriefImages(imgPath):
        # 点击 '选择图片'
        chooseImgButton = driver.find_element_by_xpath(
            '//*[@id="list"]/div[1]/div[2]/div[5]/div/div[1]/span/button'
        )
        chooseImgButton.click()

        # 传输图片
        uploadFileElement = driver.find_element_by_id("we7resourceFile")
        uploadFileElement.send_keys(imgPath)
        time.sleep(7)

        # 选择目标图片
        # Wait for upload completed
        uploadedFileName = os.path.basename(imgPath)
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="image"]/div/div[2]/div[1]/div[1]'),
                uploadedFileName,
            )
        )
        selectImage = driver.find_element_by_xpath('//*[@id="image"]/div/div[2]/div[1]')
        selectImage.click()

        # 点击 '确定'，退出对话框
        sureButton = driver.find_element_by_xpath(
            '//*[@id="material-Modal"]/div/div/div[3]/button[1]'
        )
        sureButton.click()
        time.sleep(5)

    # 上传商品简介图
    briefImageDir = rootDir + "\\synopsisImgDir"
    os.chdir(briefImageDir)
    briefImages = os.listdir(briefImageDir)

    for img in sorted(briefImages, key=os.path.getctime):
        uploadBriefImages(os.path.abspath(img))
        time.sleep(3)

    # Check '详情显示首图'
    showFirtImgInDetails = driver.find_element_by_name("thumb_first")
    showFirtImgInDetails.click()

    # Scroll to botton
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # Set sell price
    setSellPrice = driver.find_element_by_id("marketprice")
    setSellPrice.send_keys(data["售价"])

    # Set original price
    setOriginalPrice = driver.find_element_by_id("productprice")
    setOriginalPrice.send_keys(data["原价"])

    time.sleep(10)

    # Check "支持货到付款"
    cashOnDelivery = driver.find_element_by_xpath(
        '//*[@id="list"]/div[2]/div[2]/div[7]/div/label[1]/input'
    )
    cashOnDelivery.click()

    # 设置运费模板
    freightFormwork = driver.find_element_by_id("s2id_dispatchid")
    freightFormwork.click()
    time.sleep(5)

    # Locate the choosed classification
    deliveryOption = driver.find_element_by_xpath("//div[text()='满49元免费送上门']")
    deliveryOption.click()

    # Check "上架"
    releaseToMarket = driver.find_element_by_xpath(
        '//*[@id="list"]/div[2]/div[2]/div[10]/div/label[2]/input'
    )
    releaseToMarket.click()

    # 下一步
    # nextStep = driver.find_element_by_id("next")
    nextStep = driver.find_element_by_xpath('//*[@id="next"]')
    nextStep.click()
    time.sleep(5)

    # 填写 '规格/库存' 信息
    # Fill 编码
    productEncoding = driver.find_element_by_id("goodssn")
    productEncoding.send_keys(data["编码"])

    # Fill 条编
    productBarcode = driver.find_element_by_id("productsn")
    productBarcode.send_keys(data["条码"])

    # Fill 库存
    goodsInStock = driver.find_element_by_id("total")
    goodsInStock.send_keys(data["库存"])

    # Check '显示库存'
    showGoodsInStock = driver.find_element_by_id("showtotal")
    showGoodsInStock.click()

    # 下一步
    nextStep = driver.find_element_by_id("next")
    # nextStep = driver.find_element_by_xpath('//*[@id="next"]')
    nextStep.click()
    time.sleep(5)

    # Product details page
    # 商品副标题
    goodShortTitle = driver.find_element_by_id("subtitle")
    goodShortTitle.send_keys(data["商品副标题"])
    # 商品短标题
    goodShortTitle = driver.find_element_by_name("shorttitle")
    goodShortTitle.send_keys(data["商品短标题"])

    # Fill product details
    # 通过上传图片的方式
    def uploadProductDetailImg(imgPath):
        # Upload image
        # 打开插入图片按钮
        uploadImgButton = driver.find_element_by_id("edui144_body")
        uploadImgButton.click()

        # 点击 '上传图片'
        # chooseImgButton = driver.find_element_by_xpath(
        #     '//*[@id="material-Modal"]/div/div/div[2]/div[1]/form/div[2]/we7-uploader-btn'
        # )
        # chooseImgButton.click()
        # time.sleep(5)

        # 传输图片
        uploadFileElement = driver.find_element_by_id("we7resourceFile")
        uploadFileElement.send_keys(imgPath)
        time.sleep(10)

        # 选择目标图片
        # Wait for image upload complete
        uploadedFileName = os.path.basename(imgPath)
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*[@id="image"]/div/div[2]/div[1]/div[1]'),
                uploadedFileName,
            )
        )
        selectImage = driver.find_element_by_xpath('//*[@id="image"]/div/div[2]/div[1]')
        selectImage.click()

        # 点击 '确定'，退出对话框
        sureButton = driver.find_element_by_xpath(
            '//*[@id="material-Modal"]/div/div/div[3]/button[1]'
        )
        sureButton.click()
        time.sleep(5)

    # 商品详情图片
    detailImageDir = rootDir + "\\detailImageDir"
    os.chdir(detailImageDir)
    detailImages = os.listdir(detailImageDir)

    if len(detailImages) > 0:
        for img in sorted(detailImages, key=os.path.getctime):
            uploadProductDetailImg(os.path.abspath(img))

    # 通过在输入框中输入内容
    # driver.switch_to.frame("ueditor_0")
    # bodyElement = driver.find_element_by_xpath("/html/body")
    # driver.execute_script("arguments[0].innerHTML = 'My Text';", bodyElement)
    # time.sleep(5)
    # driver.switch_to.default_content()

    # Save product
    saveProduct = driver.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/div/form/div/div[4]/input"
    )
    saveProduct.click()

    print(f"上传商品 {os.path.basename(rootDir)} 成功...")

    # driver.close()


if __name__ == "__main__":
    rootDir = os.getcwd()
    uploadProduct(rootDir)
