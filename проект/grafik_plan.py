import matplotlib.pyplot as plt

tk_plan = [4340.0,4600.0,4700.0]
od_plan = [6280.0,6800.0,6700.0]
vz_plan = [5260.0,6000.0,6700.0]
tr_plan = [3720.0,3800.0,4300.0]
ga_plan = [2410.0,2700.0,3500.0]
year = [2013,2014,2018]

plt.plot(year,tk_plan,label = "Тканини")
plt.plot(year,od_plan,label = "Одяг та білизна")
plt.plot(year,vz_plan,label = "Взуття")
plt.plot(year,tr_plan,label = "Трикотаж")
plt.plot(year,ga_plan,label = "Галантерея")
plt.xlabel("Рік")
plt.ylabel("Товарообіг")
plt.title('План')
plt.legend()
plt.grid(True)


def showplot():
 plt.show()