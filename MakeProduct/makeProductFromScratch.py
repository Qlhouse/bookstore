import tkinter as tk
from tkinter import ttk
import os
from tkinter.filedialog import askdirectory


class MakeProduct:
    def __init__(self, root):
        self.root = root
        self.environment_setup()

    def environment_setup(self):
        tk.Button(self.root, text="文件目录设置", command=self.initialize_directory_environment,
                  bg="blue", fg="white").grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

    def initialize_directory_environment(self):
        self.productRootDir = askdirectory()


if __name__ == '__main__':
    root = tk.Tk()
    # print(os.getcwd())
    root.title('Make Products')
    root.geometry("800x600")
    root.resizable(width=False, height=False)
    application = MakeProduct(root)
    root.mainloop()
