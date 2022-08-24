from tkinter import Tk, Button, Entry
from tkinter.ttk import Frame
from centerWin import *

mainWindow = Tk()
searchFrame = Frame(mainWindow)

Button(mainWindow, text="Selecione a pasta:").grid(row=0,column=0)
Entry(mainWindow).grid(row=1, column=0)
Button(mainWindow, text="Realizar busca").grid(row=2,column=0)

#centerWindow(mainWindow)

mainWindow.mainloop()