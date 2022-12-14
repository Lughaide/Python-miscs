import numpy as np

with open("practice_2.txt", "r", encoding='utf-8') as f:
    print(f.name)
    print("-"*100)
    for line in f:
        for lett in line:
            print(lett.lower(), end="")
    print("-"*100)