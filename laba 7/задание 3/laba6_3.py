import matplotlib.pyplot as plt
import numpy as np
import pylab
from collections import Counter

def count_sign(sign: str):
    symvols=['.', ',', '.', '?', '!']
    for i in range(0, len(symvols)):
        xdata=[symvols[i]]
        ydata=[sign.count(symvols[i])]
        pylab.bar(xdata,ydata)
    pylab.show()

count_sign("На улице очень хорошая погода! Как думаешь,может стоит прогуляться?")