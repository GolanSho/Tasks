import os
import win32com.client
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import time

top = Tk()
top.title("תפריט 433")

L3 = Label(top, text="תפריט יומי - להב 433", font=32, bg="cyan")
L3.place(relx=0.3, rely=0.05)


def bydate():
    filebydate = rf"\\\\prfs13\\Lahav433\\הווי להב\\תפריטים\\{date}.pptx"
    pop = win32com.client.Dispatch("PowerPoint.Application")

    try:
        Presentation = pop.Presentations.Open(filebydate)
    except:
        tkinter.messagebox.showerror("שגיאה", "תאריך לא נמצא")


def todaymenu():
    today = time.strftime("%d.%m.%y")
    file = rf"\\\\prfs13\\Lahav433\\הווי להב\\תפריטים\\{today}.pptx"
    pop = win32com.client.Dispatch("PowerPoint.Application")
    try:
        Presentation = pop.Presentations.Open(file)
    except:
        tkinter.messagebox.showerror("שגיאה", "תפריט לא עודכן")


date = ""


def archive():
    topx = Toplevel(top)
    topx.title("ארכיון")
    topx.grab_set()

    def combo():
        getdate()
        bydate()
        topx.destroy()

    topx.wm_minsize(width=300, height=50)
    topx.wm_maxsize(width=300, height=150)

    L0 = Label(topx, text="Date Format: dd.mm.yy")
    L0.place(relx=0.05, rely=0.05)
    L1 = Label(topx, text=":תאריך מבוקש")
    L1.place(relx=0.6, rely=0.2)
    E1 = Entry(topx, bd=5)
    E1.place(relx=0.05, rely=0.2)

    def getdate():
        global date
        date = E1.get()

    B2 = tk.Button(topx, text="אישור", command=combo)
    B2.place(relx=0.4, rely=0.55)


B1 = tk.Button(top, text="תפריט היום", bg="blue", fg="white", padx=20, pady=20, font=32, width=10, command=todaymenu)
B1.place(relx=0.35, rely=0.25)
B2 = tk.Button(top, text="ארכיון", font=32, command=archive)
B2.place(relx=0.8, rely=0.70)

L3 = Label(top, text="בתיאבון", font=20, bg="cyan")
L3.place(relx=0.05, rely=0.70)
Credit = Label(top, text="Made By GolanSho", bg="cyan")
Credit.place(relx=0.05, rely=0.85)

image0 = tk.PhotoImage(file="atal.png")
iconatal = tk.Label(image=image0, bg="cyan")
iconatal.place(relx=0.03, rely=0.2)
image1 = tk.PhotoImage(file="lahav.png")
iconlahav = tk.Label(image=image1, bg="cyan")
iconlahav.place(relx=0.75, rely=0.2)

top.configure(bg="cyan")
top.wm_minsize(width=400, height=50)
top.wm_maxsize(width=600, height=250)
top.mainloop()
