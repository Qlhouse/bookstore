import tkinter as tk
from tkinter import PhotoImage


class Show_Image:

    def __init__(self, root):
        self.create_gui()

    def create_gui(self):
        self.show_image = tk.Toplevel(root)

        img = PhotoImage(file="scratch.png")
        tk.Label(root, image=img, text='Check Image:').grid(
            row=1, column=1, sticky=tk.W, padx=15, pady=15)

        tk.Button(root, text="关闭", command=self.destroy_window, bg="green", fg='white').grid(
            row=2, column=1, padx=20, pady=20)

        # self.show_image.mainloop()

    # return texts for searched string and subtituded string
    def destroy_window(self):
        self.show_image.destroy


if __name__ == '__main__':
    root = tk.Tk()
    # print(os.getcwd())
    root.config(background="yellow")
    root.title('Make Products')
    root.geometry("600x820")
    # root.resizable(width=False, height=False)
    application = Show_Image(root)
    # Replace_Dialogue_Window(root)
    root.mainloop()
