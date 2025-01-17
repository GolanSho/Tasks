
import random

num_gen = []

def random_gen():
    n = random.randint(1, 37)
    if n in num_gen:
        while n in num_gen:
            n = random.randint(1, 37)
    return n


ans = input('how many times? ')

for x in range(int(ans)):
    num_gen.clear()
    for i in range(6):
        to_add = random_gen()
        num_gen.append(to_add)
    num_gen = sorted(num_gen)
    num_gen.append([random.randint(1, 8)])
    
    print(num_gen)

    