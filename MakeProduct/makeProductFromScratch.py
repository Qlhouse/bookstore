import tkinter as tk
import os
import json
from tkinter.filedialog import askdirectory


class MainPage:
    def __init__(self, root):
        self.root = root
        # [TO DO] 生成配置文件，如果配置文件已存在，不用重复生成配置文件
        self.config = {}
        self.environment_setup()
        self.product_detail_frame()
        self.btn_replace()
        self.btn_clear_form()
        self.operation_frame()
        self.btn_make_product()
        self.btn_take_picture()
        self.btn_move_gallery_img()
        self.btn_move_detial_img()

    def create_gui(self):
        pass

    def environment_setup(self):
        """
        Config file: 
        + set root directory, all product data will be stored in this directory
        """
        config_file = os.path.join(os.path.dirname(__file__), "config.json")
        if os.path.exists(config_file):
            with open(config_file, 'r') as fh:
                self.config = json.load(fh)
                # print(config['rootDir'])
                self.rootDir = self.config['rootDir']
        else:
            self.productRootDir = askdirectory()
            self.config['rootDir'] = self.productRootDir
            print(self.config)
            with open(config_file, 'w') as fh:
                json.dump(self.config, fh)

    def product_detail_frame(self):
        self.labelframe = tk.LabelFrame(
            self.root, text='商品信息', bg="sky blue", font='helvetica 14', padx=20, pady=20)
        self.labelframe.grid(row=2, column=1, padx=20, pady=20, sticky='ew')

        tk.Label(self.labelframe, text='商品名称:', bg='green', fg='white').grid(
            row=1, column=1, sticky=tk.W, padx=15, pady=7)
        self.name = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.name, width=50).grid(
            row=1, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='商品副标题:', bg='green', fg='white').grid(
            row=2, column=1, sticky=tk.W, padx=15, pady=7)
        self.subName = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.subName, width=50).grid(
            row=2, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='商品短标题:', bg='green', fg='white').grid(
            row=3, column=1, sticky=tk.W, padx=15, pady=7)
        self.printerName = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.printerName, width=50).grid(
            row=3, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='单位:', bg='green', fg='white').grid(
            row=4, column=1, sticky=tk.W, padx=15, pady=7)
        self.unit = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.unit, width=50).grid(
            row=4, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='编码:', bg='green', fg='white').grid(
            row=5, column=1, sticky=tk.W, padx=15, pady=7)
        self.code = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.code, width=50).grid(
            row=5, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='条码:', bg='green', fg='white').grid(
            row=6, column=1, sticky=tk.W, padx=15, pady=7)
        self.barcode = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.barcode, width=50).grid(
            row=6, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='商品分类:', bg='green', fg='white').grid(
            row=7, column=1, sticky=tk.W, padx=15, pady=7)
        self.classification = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.classification, width=50).grid(
            row=7, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='售价:', bg='green', fg='white').grid(
            row=8, column=1, sticky=tk.W, padx=15, pady=7)
        self.price = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.price, width=50).grid(
            row=8, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='原价:', bg='green', fg='white').grid(
            row=9, column=1, sticky=tk.W, padx=15, pady=7)
        self.originalPrice = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.originalPrice, width=50).grid(
            row=9, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='库存:', bg='green', fg='white').grid(
            row=10, column=1, sticky=tk.W, padx=15, pady=7)
        self.stock = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.stock, width=50).grid(
            row=10, column=2, sticky=tk.W, padx=5, pady=7)

        tk.Label(self.labelframe, text='关键字:', bg='green', fg='white').grid(
            row=11, column=1, sticky=tk.W, padx=15, pady=7)
        self.keyword = tk.StringVar()
        tk.Entry(self.labelframe, textvariable=self.keyword, width=50).grid(
            row=11, column=2, sticky=tk.W, padx=5, pady=7)

    def btn_replace(self):
        tk.Button(self.labelframe, text="替换", command=self.replaceText,
                  bg="green", fg='white').grid(row=13, column=1, padx=5, pady=5)

    def replaceText(self):
        replace_dialog = tk.Toplevel(self.root)

        tk.Label(replace_dialog, text='查找:', bg='green', fg='white').grid(
            row=1, column=1, sticky=tk.W, padx=15, pady=15)
        original_chars = tk.StringVar()
        tk.Entry(replace_dialog, textvariable=original_chars, width=30).grid(
            row=1, column=2, sticky=tk.W, padx=5, pady=15)

        tk.Label(replace_dialog, text='替换:', bg='green', fg='white').grid(
            row=2, column=1, sticky=tk.W, padx=15, pady=15)
        subtituted_chars = tk.StringVar()
        tk.Entry(replace_dialog, textvariable=subtituted_chars, width=30).grid(
            row=2, column=2, sticky=tk.W, padx=5, pady=15)

        def replaceFunc(item):
            org_chars = original_chars.get()
            sub_chars = subtituted_chars.get()
            text = item.get()

            if org_chars in text:
                new_text = text.replace(org_chars, sub_chars)
                item.set(new_text)

        def commit():
            entryList = [self.name, self.subName,
                         self.printerName, self.keyword]

            for item in entryList:
                replaceFunc(item)

            replace_dialog.destroy()

        tk.Button(replace_dialog, text="提交", command=lambda: commit(),
                  bg="green", fg='white').grid(row=3, padx=5, pady=5)

    def btn_clear_form(self):
        tk.Button(self.labelframe, text="清除表格", command=self.clear_form,
                  bg="green", fg='white').grid(row=13, column=2, padx=5, pady=5)

    def clear_form(self):
        entry_list = [self.name, self.classification, self.subName, self.code, self.barcode,
                      self.unit, self.keyword, self.originalPrice, self.price, self.stock, self.printerName]

        for item in entry_list:
            item.set("")

    # [TO DO] Drop down list for 商品分类

    def operation_frame(self):
        self.command_frame = tk.LabelFrame(
            self.root, text='功能按钮', bg="sky blue", font='helvetica 14 bold')
        self.command_frame.grid(row=3, column=1, padx=30, pady=30, sticky='ew')

    def btn_make_product(self):
        tk.Button(self.command_frame, text="生成产品数据", command="", bg="green", fg='white').grid(
            row=1, column=1, padx=20, pady=20
        )

        def make_product():
            "Dump 'productDetail.json' "
            pass

    def btn_take_picture(self):
        tk.Button(self.command_frame, text="拍照片", command="", bg="green", fg='white').grid(
            row=1, column=2, padx=20, pady=20
        )

    def btn_move_gallery_img(self):
        tk.Button(self.command_frame, text="移动简介图", command="", bg="green", fg='white').grid(
            row=1, column=3, padx=20, pady=20
        )

    def btn_move_detial_img(self):
        tk.Button(self.command_frame, text="移动详情图", command="", bg="green", fg='white').grid(
            row=1, column=4, padx=20, pady=20
        )


if __name__ == '__main__':
    root = tk.Tk()
    # print(os.getcwd())
    root.config(background="yellow")
    root.title('Make Products')
    root.geometry("600x820")
    # root.resizable(width=False, height=False)
    application = MakeProduct(root)
    root.mainloop()


class PopupWindow:
    def __init__(self, root):
        pass
