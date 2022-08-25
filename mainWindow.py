from tkinter import Tk, Button, Entry
from tkinter.ttk import Frame
from centerWin import centerWindow
from selectFolder import selectFolder
from searchPand import sea

mainWindow = Tk()
searchFrame = Frame(mainWindow).pack()

Button(searchFrame, text="Selecione a pasta:", command=selectFolder).pack()
Entry(searchFrame).pack()
Button(searchFrame, text="Realizar busca").pack()

#centerWindow(mainWindow)

mainWindow.mainloop()