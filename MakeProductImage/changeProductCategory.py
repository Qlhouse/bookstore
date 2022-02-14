import os
import json

productData = r"D:\bookStore\productData"

for entry in os.scandir(productData):
    if entry.is_dir():
        jsonFile = os.path.join(entry.path, "productDetail.json")
        with open(jsonFile, "r", encoding="utf-8") as fh:
            productDetial = json.load(fh)
            # print(productDetial["商品分类"])

        print(
            f'{os.path.basename(entry.path)}, {productDetial["商品名称"]}, {productDetial["商品分类"]}'
        )
        changeChose = input("The product need to be changed? Type 'yes' or 'no': ")
        if changeChose == "no":
            continue
        else:
            newCategory = input("Please input new category: ")
            # productDetial.replace("商品分类", newCategory)
            productDetial["商品分类"] = newCategory
            with open(jsonFile, "w", encoding="utf-8") as fh:
                productDetial = productDetial.encode("gb2312").decode("gbk")
                json.dumps(productDetial, fh, ensure_ascii=False)
