#счеткчик символов
from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Счет символов и букв ")
root.geometry("300x100")
root.resizable(width=False, height=False) 

pr1 = tk.Label(root, text ='Введите текст')
pr1.grid(row = 0, column = 0)

    
simv = tk.Entry(root)
simv.grid(row = 0, column = 1)
def counter():
    asd = simv.get() 
    simv2 = (len(asd))
    pr2 = tk.Label(root, text = simv2 )
    pr2.place(x=50,y=50)




knop1 = tk.Button(root, text = "кол-во символов", command = counter)
knop1.grid(row = 3, column = 0)



def vivod2():
    result = simv.get()
    result = result.split(" ")
    qwerty= len(result)
    pr3 = tk.Label(root, text = qwerty)
    pr3.place(x=150,y=50)

knop2 = tk.Button(root, text = "кол-во слов", command = vivod2)
knop2.grid(row = 3, column = 1)
    

root.mainloop()

