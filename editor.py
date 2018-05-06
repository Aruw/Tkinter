from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
import sys
import os.path

root = Tk()
root.title('Editor')
menuBar = Menu(root)

def salvar():
    filename = asksaveasfile(mode='w', defaultextension='.txt')
    if filename is None:
        return
    data = text.get(1.0,END)[:-1]
    filename.write(data)
    filename.close()

def abrir():
    filename = askopenfilename()
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    text.delete(1.0, END)
    text.insert(END, data)

def limpar():
    text.delete(1.0, END)

def sobre():
    sobre = Tk()
    sobre.title('About')
    sobre.resizable(False, False)#(X,Y)
    Label(sobre, text='Simple editor.\n Free to use! xD\n Created by Aruw!', padx=20, pady=10).pack()
    sobre.mainloop()

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='Save', command=salvar)
fileMenu.add_command(label='Open', command=abrir)
fileMenu.add_command(label='Clear', command=limpar)
menuBar.add_cascade(label='File', menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=sobre)
menuBar.add_cascade(label='Help', menu=helpMenu)

frame = Frame(root)
text = Text(frame, height=400, width=400)

frame.pack()
text.pack(padx=5, pady=5, fill=BOTH, expand=TRUE)

root.config(menu=menuBar)
root.mainloop()

