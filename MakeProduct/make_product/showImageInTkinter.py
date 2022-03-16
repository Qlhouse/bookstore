from tkinter import Button, Frame, Tk, Label, BOTH
from PIL import Image, ImageTk
import numpy as np

class Show_Image(Frame):
    def __init__(self, parent, imgPath):
        Frame.__init__(self, parent)
        self.parent = parent
        self.imgPath = imgPath
        self.initUI()
        self.setImage()

    def initUI(self):
        self.parent.title("Show Image")
        self.pack(fill=BOTH, expand=1)

        self.label1 = Label(self, border=25)
        # self.label1.grid(row=1, column=1) 
        self.label1.pack(fill=BOTH, expand=1) 

        self.confirm = Button(self, text="confirm", command=self.confirm, bg="green", fg='black')
        # self.confirm.grid(row=2, column=1) 
        self.confirm.pack(fill=BOTH, expand=3) 

        self.exit = Button(self, text="exit", command=self.exit, bg="yellow", fg='black') 
        # self.exit.grid(row=2, column=2) 
        self.exit.pack(fill=BOTH, expand=3) 

    def confirm(self):
        self.destroy()

    def exit(self):
        self.destroy()

    def setImage(self):
        self.img = Image.open(self.imgPath)
        l, h = self.img.size
        # Resize image
        self.img_resized = self.img.resize((int(l/2), int(h/2)))
        text = str(l + 100) + "x" + str(h + 50)   # + "+0+0"
        print(text)
        self.parent.geometry(text)
        # photo = ImageTk.PhotoImage(self.img)
        photo = ImageTk.PhotoImage(self.img_resized) 
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
    root.geometry("800x800")
    root.mainloop()
