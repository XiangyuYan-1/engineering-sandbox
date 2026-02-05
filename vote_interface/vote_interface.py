import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def main():
    root = tk.Tk()
    root.title("Vote for your favorite food")
    root.geometry("650x1155")
    
    
    img = Image.open(r"C:\Users\15691\epf-programming\python projet\engineering-sandbox\vote_interface\background.jpg")
    bg_img = ImageTk.PhotoImage(img)

    root.bg_img = bg_img  
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)



    root.mainloop()



if __name__ == "__main__":
    main()