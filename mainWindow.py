from tkinter import Tk, Button, Entry
from tkinter.ttk import Frame
from centerWin import centerWindow
from selectFolder import selectFolder

mainWindow = Tk()
searchFrame = Frame(mainWindow)

Button(searchFrame, text="Selecione a pasta:", command=selectFolder)
Entry(searchFrame)
Button(searchFrame, text="Realizar busca")

#centerWindow(mainWindow)

mainWindow.mainloop()