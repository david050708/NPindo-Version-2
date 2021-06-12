import tkinter as tk
from tkinter import *
import pyttsx3

root = tk.Tk()
root.geometry("700x700")
root.title("NPindo IDE")

label1 = Label(root,text="Console").pack()
console = Entry(root,width=50,fg="black",bg="white")
console.pack(padx=10,pady=20)

label2 = Label(root,text="GUI Title").pack()
gui_title = Entry(root,width=50,fg="black",bg="white")
gui_title.pack(padx=10,pady=20)

label3 = Label(root,text="GUI Geometry").pack()
gui_geometry = Entry(root,width=50,fg="black",bg="white")
gui_geometry.pack(padx=10,pady=20)

label4 = Label(root,text="Speaker").pack()
speak_text = Entry(root,width=50,fg="black",bg="white")
speak_text.pack(padx=10,pady=20)

label5 = Label(root,text="Label Creator").pack()
label_gui = Entry(root,width=50,fg="black",bg="white")
label_gui.pack(padx=10,pady=20)

def run_in_console():
    print(console.get())

def speaker():
    pyttsx3.speak(speak_text.get())

def create_window():
    root = tk.Tk()
    root.title(gui_title.get())
    root.geometry(gui_geometry.get())

    root.mainloop()

def lbl_creator():
    root = tk.Tk()
    root.title(gui_title.get())
    root.geometry(gui_geometry.get())

    label1 = Label(root,text=label_gui.get()).pack()

    root.mainloop()


b1 = tk.Button(root,text="Run in Console",fg="black",bg="grey",command=run_in_console).pack()
b2 = tk.Button(root,text="GUI CREATOR",fg="black",bg="grey",command=create_window).pack()
b3 = tk.Button(root,text="Speak",fg="black",bg="grey",command=speaker).pack()
b4 = tk.Button(root,text="Create Label",fg="black",bg="grey",command=lbl_creator).pack()
b5 = tk.Button(root,text="Close",fg="black",bg="grey",command=exit).pack()

root.mainloop()
