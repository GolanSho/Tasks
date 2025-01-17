import re
import requests
from tkinter import *

top = Tk()
top.title("SSL Checker")

L0 = Label(top, text="Host to check: ")
L0.place(relx=0.08, rely=0.1)
global E1
E1 = Entry(top, bd=5)
E1.place(relx=0.35, rely=0.1)

def check_host():
    while True:
        host = E1.get()
        if host == "":
            break
        out = ""
        while "Issuer" not in out:
            res = requests.get(f"https://www.ssllabs.com/ssltest/analyze.html?d={host}&latest")
            out = res.text

        subject = re.search(r'(?<=Subject</td>\n\s{12}<td class="tableCell" title="CN&#61;).*(?=")', out)
        ip = re.search(r'(?<= <span class=ip> \().*(?=\))', out)
        vuntil = re.search(r'(?<=Valid until</td>\n\t{3}\s{4}<td class="tableCell">).*\)', out)
        issuer = re.search(r'(?<=Issuer</td>\n\t{3}<td class="tableCell" title="CN&#61;).*?(?=,)', out)
        cln_issuer = re.sub('&#39;', '\'', issuer[0])

        L1 = Label(top, text=f"Subject: {subject[0]}").place(relx=0.06, rely=0.3)
        L2 = Label(top, text=f"IP: {ip[0]}").place(relx=0.06, rely=0.45)
        L3 = Label(top, text=f"Valid until: {vuntil[0]}").place(relx=0.06, rely=0.6)
        L4 = Label(top, text=f"Issuer: {cln_issuer}").place(relx=0.06, rely=0.75)
        break


B = Button(top, text="Check", command=check_host)
B.place(relx=0.75, rely=0.1, height=27, width=70)

top.wm_minsize(width=450, height=50)
top.wm_maxsize(width=450, height=190)

top.mainloop()