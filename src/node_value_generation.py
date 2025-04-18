import random

def firstN(val, off):
    if val == 0:
        return 1.0
    else:
        return 2*val + off

def randGen(val, off):
    return round(val + 0.1 + random.random()*10, 1) 