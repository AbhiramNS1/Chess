import Chess
from tkinter import *
new=Chess.Tk()
new.title("Chess")
new.geometry("500x500")
new.iconbitmap(Chess.resource("logo.ico"))
bg=Chess.PhotoImage(file=Chess.resource(r"im.png"))
undo=Chess.PhotoImage(file=Chess.resource("u0.png"))
iconpack=1

def canvas(head):
	global can
	try:can.destroy()
	except:pass
	can=Canvas(new,width=560,height=560)
	can.pack(fill="both",expand=True)
	can.create_image(0,0,image=bg,anchor="nw")
	can.create_text(250,75,text=head,fill="red",font=("Times",50))

def buttons(n,name,fun):
	for i in range(n):
		B2=Button(can,text=name[i],font=("verdana",10),width=20,borderwidth=0,command=fun[i],activebackground="#7CFF0A")
		buutonwin1=can.create_window(170,190+i*60,window=B2,anchor="nw")

def play():
	can.destroy()
	new.geometry("635x580")
	Chess.mode="Co"
	h=Chess.chess(new)
	h.loadimage(iconpack)
	h.board()
	B=Button(new,command=h.undo,image=undo,anchor="n")
	B.grid(row=0,column=9)

	
def multiplayer():
	can.destroy()
	new.geometry("600x580")
	h=Chess.chess(new)
	h.loadimage(iconpack)
	h.board()
	B=Button(new,command=h.undo,image=undo)
	B.grid(row=0,column=9)


def about():
	canvas("About Chess v1.1")
	can.create_text(250,200,text="Chess v1.1 has more modified features than the older version.\nChess v1.1 have undo feature and a computer engine that\n will play chess with us.But it is a base vertion\n (chess engine v1.0)\nThe buttons,chess board,and size of window are modified",fill="yellow",font=("times",15))
	B2=Button(can,text="back to menu",font=("verdana",10),width=20,borderwidth=0,command=mainscreen,activebackground="#7CFF0A")
	buutonwin1=can.create_window(170,300,window=B2,anchor="nw")

def settings():
	def chc():
		def c1():Chess.highlight="red"
		def c2():Chess.highlight="green"
		def c3():Chess.highlight="blue"
		
		Chess.highlight="red"
		canvas("Color")
		buttons(4,["red","green","blue","back"],[c1,c2,c3,settings])
	def cip():
		def ico2():
			global iconpack
			iconpack=2
		
		canvas("Icon pack")
		buttons(3,["pack1","pack2","back to menu"],[None,ico2,settings])
	
	canvas("Settings")
	buttons(3,["change highlight color","chage icon pack","back to menu"],[chc,cip,mainscreen])


def mainscreen():
	canvas("CHESS")
	buttons(4,["play with computer","multiplayer","settings","about"],[play,multiplayer,settings,about])

if __name__=="__main__":
	mainscreen()
	
new.mainloop()


