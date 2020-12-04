import pandas as pd
datos = pd.read_csv('Day 3/input.txt', header=None).values
datos=[list(x)[0] for x in datos]

for x in datos:
    print(x[0])
    break

