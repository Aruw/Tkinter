import tkinter as tk


#Root Window
root = tk.Tk()
root.title("Widgets!")
root.geometry("400x900+670+50")



#Menu
menuButton = tk.Menubutton(root, text="File", )
menuButton.pack()
menu = tk.Menu(menuButton, tearoff=0)
menuButton['menu'] = menu
menu.add('command', label="Open")




#Frame 1
frame1 = tk.Frame(root)

label = tk.Label(frame1, text="This is a label")

tv = tk.StringVar() 
entry = tk.Entry(frame1, textvariable=tv)
tv.set('I am an entry widget')

button = tk.Button(frame1, text="Button here!")

checkButton = tk.Checkbutton(frame1, text="Checkbutton B is lowcase")

radioButton1 = tk.Radiobutton(frame1, text="Male", value=1)
radioButton2 = tk.Radiobutton(frame1, text="Female", value=2)

optionMenu = tk.OptionMenu(frame1, "Default", "BR", "EUA", "JP", "SELA", "PA")

#bitmap = tk.BitmapImage(file="D:\\Tkinter\\image.jpg")




#Frame 2
frame2 = tk.Frame(root)

#photoImage = tk.PhotoImage(file="")

listBox = tk.Listbox(frame2, height=4)
for line in ["Amazonas", "São Paulo", "Rio de Janeiro", "Rio Grande do sul"]:
    listBox.insert(tk.END, line)

spinBox = tk.Spinbox(frame2, values=(1, 2, 4, 6, 8, 10))

scale = tk.Scale(frame2, from_=0.0, to=100.0, label="Parece um SeekBar...", orient=tk.HORIZONTAL)

labelFrame = tk.LabelFrame(frame2, text="LabelFrame Widget", padx=10, pady=10)
labframe = tk.Label(labelFrame, text="Ola")

message = tk.Message(frame2, text="I'm a message widget")   #similar in its functionality to the Label widget, but it is more flexible in displaying text




#Frame 3
frame3 = tk.Frame(root)

text = tk.Text(frame3, height=4, width=40)
#fhandle = open("content.txt")
#lines = fhandle.read()
#fhandle.close()
#text.insert(tk.END, lines)

scrollBar = tk.Scrollbar(frame3, orient=tk.VERTICAL, command=text.yview)

canvas = tk.Canvas(frame3, bg="white", width=340, height=80)
canvas.create_oval(20,15,60,60, fill='red')
canvas.create_oval(40,15,60,60, fill='grey')
canvas.create_text(130, 38, text='I am a Canvas Widget', font=('arial', 8, 'bold'))

m1 = tk.PanedWindow()
left = tk.Text(m1, height=6, width =15)
m1.add(left)
m2 = tk.PanedWindow(m1, orient=tk.VERTICAL)
m1.add(m2)
top = tk.Text(m2, height=3, width =3)
m2.add(top)
bottom = tk.Text(m2, height=3, width =3)
m2.add(bottom)




#Packs
frame1.pack()
label.pack()
entry.pack()
button.pack()
checkButton.pack()
radioButton1.pack()
radioButton2.pack()
optionMenu.pack()
#bitmap.pack()


frame2.pack()
#photoImage.show()
listBox.pack()
spinBox.pack()
scale.pack()
labelFrame.pack()
labframe.pack()
message.pack()


frame3.pack()
text.pack()
scrollBar.pack()
canvas.pack()
m1.pack(fill=tk.BOTH, expand=2)


#Initialize
root.mainloop()
