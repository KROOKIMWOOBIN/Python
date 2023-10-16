import random as rd

def TarkovRandom():
    num = rd.randrange(1, 8)
    ch = ["랩", "커스텀", "등대", "인터체인지", "리저브", "해안선", "우드"]
    print(f"{num}번 {ch[num - 1]}")

TarkovRandom()