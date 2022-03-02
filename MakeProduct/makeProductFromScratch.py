import tkinter as tk
import os
import json
from tkinter.filedialog import askdirectory


class MainPage:
    def __init__(self, root):
        # self.root = root
        # [TO DO] 生成配置文件，如果配置文件已存在，不用重复生成配置文件
        self.config = {}
        self.environment_setup()
        self.create_gui()

    def create_gui(self):
        self.product_detail_frame()
        self.command_frame()

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
            root, text='商品信息', bg="sky blue", font='helvetica 14', padx=20, pady=20)
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

        tk.Button(self.labelframe, text="替换", command=self.replaceText,
                  bg="green", fg='white').grid(row=13, column=1, padx=5, pady=5)

        tk.Button(self.labelframe, text="清除表格", command=self.clear_form,
                  bg="green", fg='white').grid(row=13, column=2, padx=5, pady=5)

    def command_frame(self):
        self.command_frame = tk.LabelFrame(
            root, text='功能按钮', bg="sky blue", font='helvetica 14 bold')
        self.command_frame.grid(row=3, column=1, padx=30, pady=30, sticky='ew')

        tk.Button(self.command_frame, text="生成产品数据", command="", bg="green", fg='white').grid(
            row=1, column=1, padx=20, pady=20
        )

        tk.Button(self.command_frame, text="拍照片", command="", bg="green", fg='white').grid(
            row=1, column=2, padx=20, pady=20
        )

        tk.Button(self.command_frame, text="移动简介图", command="", bg="green", fg='white').grid(
            row=1, column=3, padx=20, pady=20
        )

        tk.Button(self.command_frame, text="移动详情图", command="", bg="green", fg='white').grid(
            row=1, column=4, padx=20, pady=20
        )

    def replaceText(self):
        entryList = [self.name, self.subName,
                     self.printerName, self.keyword]
        org_chars, sub_chars = Replace_Dialogue_Window(
            self.labelframe).get_inputs()
        print(org_chars, sub_chars)

        for item in entryList:
            text = item.get()
            if org_chars in text:
                new_text = text.replace(org_chars, sub_chars)
                item.set(new_text)

    def clear_form(self):
        entry_list = [self.name, self.classification, self.subName, self.code, self.barcode,
                      self.unit, self.keyword, self.originalPrice, self.price, self.stock, self.printerName]

        for item in entry_list:
            item.set("")

    # [TO DO] Drop down list for 商品分类

    def make_product():
        "Dump 'productDetail.json' "
        pass


class Replace_Dialogue_Window:

    def __init__(self, root):
        # self.root = root
        self.create_gui()

    def create_gui(self):
        self.replace_dialog = tk.Toplevel(root)

        tk.Label(self.replace_dialog, text='查找:', bg='green', fg='white').grid(
            row=1, column=1, sticky=tk.W, padx=15, pady=15)
        self.original_chars = tk.StringVar(self.replace_dialog)
        tk.Entry(self.replace_dialog, textvariable=self.original_chars, width=30).grid(
            row=1, column=2, sticky=tk.W, padx=5, pady=15)

        tk.Label(self.replace_dialog, text='替换:', bg='green', fg='white').grid(
            row=2, column=1, sticky=tk.W, padx=15, pady=15)
        self.subtituted_chars = tk.StringVar(self.replace_dialog)
        tk.Entry(self.replace_dialog, textvariable=self.subtituted_chars, width=30).grid(
            row=2, column=2, sticky=tk.W, padx=5, pady=15)

        tk.Button(self.replace_dialog, text="提交", command=self.replace_dialog.destroy,
                  bg="green", fg='white').grid(row=3, padx=5, pady=5)

        # self.replace_dialog.mainloop()

    def get_inputs(self):
        self.replace_dialog.deiconify()
        self.replace_dialog.wait_window()
        self.org_chars = self.original_chars.get()
        self.sub_chars = self.subtituted_chars.get()
        return self.org_chars, self.sub_chars


if __name__ == '__main__':
    root = tk.Tk()
    # print(os.getcwd())
    root.config(background="yellow")
    root.title('Make Products')
    root.geometry("600x820")
    # root.resizable(width=False, height=False)
    application = MainPage(root)
    # Replace_Dialogue_Window(root)
    root.mainloop()
