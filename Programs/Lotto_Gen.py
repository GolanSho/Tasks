import random
from tkinter import *
import mysql.connector

top = Tk()
top.title("Lotto Numbers Gen")

L0 = Label(top, text="Number of times: ")
L0.place(relx=0.08, rely=0.2)
global E1
E1 = Entry(top, bd=5)
E1.place(relx=0.35, rely=0.2)
num_gen = []
extra_num = []

global gen_mode
gen_mode = IntVar()

r1 = Radiobutton(top, text='Random', variable=gen_mode, value=1).place(relx=0.2, rely=0.1)
r2 = Radiobutton(top, text='From DB', variable=gen_mode, value=2).place(relx=0.5, rely=0.1)

def random_gen():
    n = random.randint(1, 37)
    if n in num_gen:
        while n in num_gen:
            n = random.randint(1, 37)
    return n

def best_numbers():
    db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Iolredi8b4!",
    database="old_res"
    )
    cursor = db.cursor()

    numbers_stats = [
        [], [], [], [], [], [], []
    ]

    index = 0
    num_gen.clear()
    extra_num.clear()

    query = "SELECT num1, num2, num3, num4, num5, num6, num7 FROM numbers"
    cursor.execute(query)
    db_rows = cursor.fetchall()
    for row in db_rows:
        for num in range(7):
            numbers_stats[num].append(row[num])
    
    for pos in numbers_stats:
        choosen_num = pos.pop(random.randint(0, len(pos)))
        if index == 6:
            extra_num.append(int(choosen_num))
            continue
        elif choosen_num in num_gen:
            while choosen_num in num_gen:
                choosen_num = pos.pop(random.randint(0, len(pos)))
        num_gen.append(int(choosen_num))
        index+=1

    return [num_gen, extra_num]

def gen_numbers():
    num_gen = []

    L1 = Listbox(top, selectmode=SINGLE, height=8, font=10, width=25)
    L1.place(relx=0.28, rely=0.35)
    if gen_mode.get() == 1:
        for x in range(int(E1.get())):
            num_gen.clear()
            for i in range(6):
                to_add = random_gen()
                num_gen.append(to_add)
            num_gen = sorted(num_gen)
            extra_num = random.randint(1, 8)
            L1.insert(x, f"{num_gen}  [{extra_num}]")
    elif gen_mode.get() == 2:
       for x in range(int(E1.get())):
            num_gen = best_numbers()
            L1.insert(x, f"{num_gen[0]}   {num_gen[1]}")

B = Button(top, text="Generate", command=gen_numbers)
B.place(relx=0.75, rely=0.2, height=27, width=70)

top.wm_minsize(width=450, height=280)
top.wm_maxsize(width=450, height=280)

top.mainloop()