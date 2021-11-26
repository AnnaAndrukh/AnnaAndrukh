import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab

test = "На улице было тепло погода как раз подходила для прогулки"
char_list = list(test)
xdata = pd.DataFrame({'letters': char_list})
xdata['num'] = 1
xdata = xdata.groupby('letters').sum().sort_values('num', ascending=False) / len(xdata)

plt.bar(xdata.index, xdata.num, width=0.5)
plt.show()






