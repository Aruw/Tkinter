from tkinter import *
import random
import string

def gerarLetra(event):
    letra = random.choice(string.ascii_uppercase)
    print(letra)
    label1.config(text=letra)

def gerarNumero(event):
    numero = random.randrange(1,999)
    print(numero)
    label2.config(text=numero)

def gerarDecimal(event):
    decimal = random.random()
    print(decimal)
    label3.config(text=decimal)

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

button1 = Button(frame1, text='Gerar letra!')
label1 = Label(frame1, text='')

button2 = Button(frame2, text='Gerar Número!')
label2 = Label(frame2, text='')

button3 = Button(frame3, text='Gerar decimal!')
label3 = Label(frame3, text='')

button1.bind("<Button-1>", gerarLetra)
button2.bind("<Button-1>", gerarNumero)
button3.bind("<Button-1>", gerarDecimal)

frame1.pack(side=LEFT)
button1.pack()
label1.pack()

frame2.pack(side=LEFT)
button2.pack()
label2.pack()

frame3.pack(side=RIGHT)
button3.pack()
label3.pack()

root.mainloop()
