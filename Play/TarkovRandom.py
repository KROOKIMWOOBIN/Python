import random as rd
import time
import tkinter

def TarkovRandom():
    num = rd.randrange(1, 7)
    ch = ["랩", "커스텀", "인터체인지", "리저브", "해안선", "우드"]
    print(f"{num}번 {ch[num - 1]}")

for i in range(3):
    TarkovRandom()
    time.sleep(0.1)