
import os
import win32com.client
import tkinter as tk
from tkinter import *
import win32gui

top = Tk()
top.title("Doc2Pdf")

L0 = Label(top, text="Enter a Full Path to the files")
L0.place(relx=0.1, rely=0.02)

L1 = Label(top, text="Source Folder")
L1.place(relx=0.05, rely=0.2)
E1 = Entry(top, bd=5)
E1.place(relx=0.45, rely=0.2)


def l1():
    e1 = E1.get()
    return e1


L2 = Label(top, text="Destination")
L2.place(relx=0.05, rely=0.4)
E2 = Entry(top, bd=5)
E2.place(relx=0.45, rely=0.4)


def l2():
    e2 = E2.get()
    return e2


Credit = Label(top, text="Made By GolanSho")
Credit.place(relx=0.1, rely=0.7)


def con():
    total = 0
    conver = 0
    failed = []
    pathin = fr"{l1()}".replace("/", "\\")
    pathout = fr"{l2()}".replace("/", "\\")

    win32gui.MessageBox(0, f"Converting from {pathin} to {pathout}", "Doc2Pdf", 0)

    word = win32com.client.Dispatch('Word.Application')

    for dirpath, dirnames, filenames in os.walk(pathin):
        for f in filenames:
            try:
                if f.lower().endswith(".docx"):
                    new_name = f.replace(".docx", ".pdf")
                    in_file = (dirpath + '/' + f)
                    new_file = (pathout + '/' + new_name)
                    doc = word.Documents.Open(in_file)
                    doc.SaveAs(new_file, FileFormat=17)
                    doc.Close()
                    conver += 1
                if f.lower().endswith(".doc"):
                    new_name = f.replace(".doc", ".pdf")
                    in_file = (dirpath + '/' + f)
                    new_file = (pathout + '/' + new_name)
                    doc = word.Documents.Open(in_file)
                    doc.SaveAs(new_file, FileFormat=17)
                    doc.Close()
                    conver += 1
            except:
                failed.append(f)
            total += 1
    word.Quit()

    win32gui.MessageBox(0, f"{conver} files converted out of {total}", "Doc2Pdf", 0)
    if conver != total:
        win32gui.MessageBox(0, f"There was an access problem in: {failed}", "Doc2Pdf", 0)


B = tk.Button(top, text="Convert", command=con)
B.place(relx=0.4, rely=0.6, height=50, width=100)

top.wm_minsize(width=400, height=50)
top.wm_maxsize(width=400, height=190)

top.mainloop()

