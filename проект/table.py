from prettytable import PrettyTable

from data import dt

x = PrettyTable()

x.field_names = ['Найменування','Рік','План(товарооб.)','Очік.Виконан.(товарооб.)','План(доход)','Очік.викон.(доход)']

for i in range (0, len(dt)):

    x.add_rows(
        [
            dt[i]
        ]
    )
def operatabble():
    print('\nВАЛОВИЙ ДОХОД УНІВЕРМАГУ')
    print(x)