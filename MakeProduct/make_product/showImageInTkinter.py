from tkinter import Frame, Tk, Label, BOTH
from PIL import Image, ImageTk
import numpy as np

class Show_Image(Frame):
    def __init__(self, parent, imgPath):
        Frame.__init__(self, parent)
        self.parent = parent
        self.imgPath = imgPath
        self.initUI()

    def initUI(self):
        self.parent.title("Show Image")
        self.pack(fill=BOTH, expand=1)

        self.label1 = Label(self, border=25)
        # self.label2 = Label(self, border=25) 
        self.label1.grid(row=1, column=1) 
        # self.label2.grid(row=1, column=2) 
        self.setImage()
 

    def setImage(self):
        self.img = Image.open(self.imgPath)
        self.img_resized = self.img.resize()
        self.I = np.asarray(self.img)
        l, h = self.img.size
        text = str(2*l + 100) + "x" + str(h + 50) + "+0+0"
        self.parent.geometry(text)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
        self.label1.image = photo

 
    # def onNegative(self):
    #     # Image Negative Menu callback
    #     I2 = 255 - self.I
    #     img = Image.fromarray(np.uint8(I2))
    #     photo2 = ImageTk.PhotoImage(img)
    #     self.label2.configure(image=photo2) 
    #     self.label2.image = photo2


    
if __name__ == "__main__":
    root = Tk()
    Show_Image(root, "afterRmBg2.png")
    root.geometry("320x240")
    root.mainloop()
