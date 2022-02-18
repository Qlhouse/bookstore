"""
Design:
  + Product Detail Window 
    Write down product detail, create directory with product ISBN, dump product 
    details a json file, file name: 'productDetail.json'.
  + Move Images Window
"""
import tkinter as tk
from tkinter import ttk


class ProductDetail(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('800x700')
        self.title('Product Detail Window')
        self.configure(bg="#ffbf00")
        self.rowconfigure

    # Place Button
    def generate_product(self):
        ttk.Button(self, text="生成商品", command=self.make_product)

    def make_product(self):
        window = ProductDetail(self)
        window.grab_Set()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x900')
        self.title('Main Window')
