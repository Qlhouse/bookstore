import shutil
import os

originalDir = r"D:\bookStore\productData"
destinationDir = r"D:\bookStore\productDataBackup"

uploadSuccess = r"D:\bookStore\uploadProductToWebsite\uploadSuccess.txt"


def moveSuccessedDirClearRecord():
    with open(uploadSuccess, "r") as fh:
        for line in fh:
            foldPath = os.path.join(originalDir, line.strip())
            try:
                shutil.move(foldPath, destinationDir)
            except Exception as e:
                print(e)
            # print(line.strip())

    # 清空成功传输的文件夹
    with open(uploadSuccess, "w") as fh:
        fh.truncate()


if __name__ == "__main__":
    moveSuccessedDirClearRecord()
