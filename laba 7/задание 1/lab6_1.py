import matplotlib.pyplot as plt
import numpy as np

fig, ax=plt.subplots()

x=np.linspace(-5,5)
y=1/x*np.sin(5*x)
ax.plot(x,y)

plt.show()

