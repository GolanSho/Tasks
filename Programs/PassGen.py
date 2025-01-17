import random
import string
from tkinter import *


top = Tk()
top.title("Pass Generator")

L0 = Label(top, text="How many Characters? ")
L0.place(relx=0.06, rely=0.1)

global ans
ans = IntVar()

global passwd_ls

Radiobutton(top, text='6', variable=ans, value=6).place(relx=0.4, rely=0.1)
Radiobutton(top, text='8', variable=ans, value=8).place(relx=0.5, rely=0.1)
Radiobutton(top, text='10', variable=ans, value=10).place(relx=0.6, rely=0.1)
Radiobutton(top, text='12', variable=ans, value=12).place(relx=0.7, rely=0.1)
Radiobutton(top, text='16', variable=ans, value=16).place(relx=0.8, rely=0.1)

E1 = Entry(top, bd=5)
E1.place(relx=0.5, rely=0.3)

def f_pass_gen():
    E1.delete(0, END)
    passwd = ''
    passwd_ls = []
    for x in range(10):
        for i in range(ans.get()):

            num = random.randint(0, 9)

            az = string.ascii_lowercase
            azrand = random.choice(az)
            AZ = string.ascii_uppercase
            AZrand = random.choice(AZ)
        
            char_list = [num, azrand, AZrand]
            char_toadd = str(random.choice(char_list))
        
            if char_toadd in passwd:
                num = random.randint(0, 9)
                azrand = random.choice(az)
                AZrand = random.choice(AZ)
                char_list = [num, azrand, AZrand]
                char_toadd = str(random.choice(char_list))
            passwd = passwd + char_toadd
        passwd_ls.append(passwd)
        passwd = ''
    E1.insert(0, passwd_ls[0])
    
    L = Listbox(top, selectmode=SINGLE, height=5)
    
    for z in range(10):
        L.insert(z, passwd_ls[z])
    def chse_pass(event):
        pas = L.curselection()
        pas = L.get(pas)
        E1.delete(0, END)
        E1.insert(0, pas)
    
    L.place(relx=0.5, rely=0.5)
    L.bind('<<ListboxSelect>>', chse_pass)


def show_ip():
    import re
    import requests

    res = requests.get('http://qip.co.il/')

    qip_out = res.text
    ip = re.search(r'(.*?Your IP.*)', qip_out)
    cln_ip = re.sub('</?h1>|</?b>', '', ip[0])
    
    L2 = Label(top, text=cln_ip).place(relx=0.06, rely=0.8)


B = Button(top, text="Generate", command=f_pass_gen)
B.place(relx=0.1, rely=0.25, height=50, width=100)

B2 = Button(top, text="Whats My IP?", command=show_ip)
B2.place(relx=0.1, rely=0.6, height=30, width=100)

top.wm_minsize(width=400, height=50)
top.wm_maxsize(width=400, height=190)

top.mainloop()