from tkinter import *
import tkinter as tk

from matplotlib.pyplot import title
from grafik_plan import showplot
from grafik_vukon import showax
from table import operatabble
from to_json import convertTojson
from to_json import convertInjson

win = tk.Tk()
win.geometry(f"300x300")
win.title('Аналіз валового доходу')
win.configure(bg = 'DarkOliveGreen4')

def open_graf():
    showplot()
    showax()

btn1=tk.Button(win,text='Відкрити графіки плану та виконання', command=open_graf)
btn1.configure(bg = 'DarkOliveGreen2')
btn1.pack()



def open_table():
    operatabble()
    win_3 = tk.Tk()
    win_3.geometry('200x100')
    win_3.title('Таблиця')
    win_3.configure(bg = 'DarkOliveGreen4')
    lbl=Label(win_3)
    lbl.configure(text="Таблиця в консолі")
    lbl.place(x=0,y=0)
    win_3.mainloop()

btn3=tk.Button(win,text='Відкрити таблицю', command=open_table)
btn3.configure(bg = 'DarkOliveGreen2')
btn3.pack()

def open_tov():
    convertTojson()
    win_4 = tk.Tk()
    win_4.geometry('356x70')
    win_4.title('Ціна')
    win_4.configure(bg = 'DarkOliveGreen4')
    lbl=Label(win_4)
    lbl.configure(text="Файл у форматі JSON сформовано")
    lbl.place(x=0,y=0)
    win_4.mainloop()


btn4=tk.Button(win,text='Відкрити ціну(JSON)', command=open_tov)
btn4.configure(bg = 'DarkOliveGreen2')
btn4.pack()

def open_pr():
    convertInjson()
    win_5 = tk.Tk()
    win_5.geometry('356x70')
    win_5.title('Товар')
    win_5.configure(bg = 'DarkOliveGreen4')
    lbl=Label(win_5)
    lbl.configure(text="Файл у форматі JSON сформовано")
    lbl.place(x=0,y=0)
    win_5.mainloop()

btn5=tk.Button(win,text='Відкрити список товарів(JSON)', command=open_pr)
btn5.configure(bg = 'DarkOliveGreen2')
btn5.pack()
win.mainloop()
