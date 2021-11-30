import matplotlib.pyplot as plt

fig, ax = plt.subplots()

tk_vuk = [4420.0,4640.0,4625.0]
od_vuk = [6720.0,7400.0,6630.0]
vz_vuk = [5854.0,6250.0,6500.0]
tr_vuk = [3682.0,3850.0,4500.0]
ga_vuk = [2694.0,3000.0,3590.0]
year = [2013,2014,2018] 

ax.plot(year,tk_vuk,label = "Тканини1")
ax.plot(year,od_vuk,label = "Одяг та білизна1")
ax.plot(year,vz_vuk,label = "Взуття1")
ax.plot(year,tr_vuk,label = "Трикотаж1")
ax.plot(year,ga_vuk,label = "Галантерея1")
plt.xlabel("Рік")
plt.ylabel("Товарообіг")
plt.legend()
plt.title('Очікуване виконання')
plt.grid(True)

def showax():
 plt.show()