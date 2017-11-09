import tkinter				#'t'kinter minusculo para trabalhar com Python 2.7

window = tkinter.Tk()

window.title("Window Title")
window["background"] = "gray"		#Alter the key - like it is a dictionary
window.geometry("400x400+250+250")	#Set the height width and the (0,0) start point - WxH+L+T you can use only +L+T

window.mainloop()			#The program stops here, until the window is closed
