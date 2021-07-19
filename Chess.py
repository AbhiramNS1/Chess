from tkinter import *
import os
import sys
import time
from random import randint
button=[]
BKP=32
WKP=39
Turn="White"
highlight="yellow"
t_p=[]
selected=0
p=70
p_id=70
undo=[]
mode="Mu"
pack=1
def resource(relpath):
		try:
			base_path=sys._MEIPASS
		except Exception:
			base_path=os.path.abspath(".")
		return os.path.join(base_path,relpath)



class chess():
	def __init__(self,root):
		self.root=root
	def board(self):
		global WKP,BKP,t_p,undoim
		
		self.A=Frame(self.root)
		self.A.grid(row=0,column=0)
		for j in range(8):
			for i in range(8):
				v=j*8+i
				position="empty"
				global clr
				if i%2==0: 
					if j%2==0:
						if pack==1:
							clr="Black"
						elif pack==2:
							clr="#ff0041"
					else:
						if pack==1:
							clr="White"
						elif pack==2:
							clr="#1ba8f0"
							

				else:
					if j%2==0:clr="White"	
					else:clr= "Black"	
				if(i==1)|(i==6):position="soldier"
				elif(((v==8)|(v==15))|((v==48)|(v==55))):position="horse"
				elif(((v==7)|(v==0))|((v==56)|(v==63))):position="rock"
				elif(v==16)|(v==40)|(v==23)|(v==47):position="elephant"
				elif(v==31)|(v==24):position="queen"
				elif(v==39)|(v==32):position="king"
				#defining the team of each coloum
				if(i==0)|(i==1):t="Black"
				elif(i==6)|(i==7):t="White"
				else:
					t="null"



				B=Button(self.A,bg=clr,image=self.imager(t,position),command=lambda v=v:self.click(v),borderwidth=0)
				B.grid(row=i,column=j)
				
			

				button.append(B)
				if position=="soldier":
					t_p.append([position,t,i+1,j+1,clr,1,self.imager(t,position)])
				else:
					t_p.append([position,t,i+1,j+1,clr,0,self.imager(t,position)])
		
	def click(self,index):
		global selected,p_s_po,p_s_t,p_id,Turn,p_s_img,var,BKP,WKP,selwin,undo
		p=index
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		Label(self.root,text=str(p)+" team="+team+" position="+position+" row="+str(ro)+" coloum="+str(co)).grid(row=1,column=0)
		self.checks()
		def move():
			global Turn,BKP,WKP,mode
			
			if t_p[p][0]!="empty":undo.insert(0,[p,p_id,[t_p[p][0],t_p[p][1]]])
			else:undo.insert(0,[p,p_id,[]])
			button[p].config(image=p_s_img)
			t_p[p][6]=p_s_img
			t_p[p][0]=p_s_po
			t_p[p][1]=p_s_t
			if t_p[p_id][0]=="king":
				if Turn=="Black":BKP=p
				elif Turn=="White":WKP=p
			if t_p[p_id][4]=="Black":
				button[p_id].config(image=Bempty)
				t_p[p_id][6]=Bempty
			else:
				button[p_id].config(image=Wempty)
				t_p[p_id][6]=Wempty
			if Turn=="White":Turn="Black"
			elif Turn=="Black":Turn ="White"
			t_p[p_id][0]="empty"
			t_p[p_id][1]="null"
			if mode=="Co":self.selfmove()

		if selected==0:
			global p_sel,t_sel
			p_sel=position
			t_sel=team
			if t_sel!=Turn or "selwin" in globals():return ""
			
			if t_sel!="null":
				selected=1
				var=self.pow(p_sel,p,"real")


				if(self.check("",Turn)!="none"):
					if (len(self.config_analysis(Turn))==0):
						self.root.config(bg="red")
						for i in range(64):
							if t_p[i][1]==Turn:button[i].config(bg="red")
						return ""

				if(position=="king"):
					var=[self.common(self.config_pos(Turn,p,position),var)]
				else:
					var=[self.common(self.config_pos(Turn,p,position),var)]


				for i in var:
					self.clr(i)	
		elif selected==1:
			selected=0
			for i in var:
				self.rclr(i)
			if p_s_po=="soldier":
				for i in range(8):
					if ((p==8*i)|(p==8*i+7))&self.srch(p):
						self.selwin(p_s_t,p)
						return ""
			if self.srch(p):move()
		self.checks()
			
		p_s_po=p_sel
		p_s_t=t_sel
		p_id=p
		p_s_img=t_p[p][6]
	def common(self,l1,l2):
		#intersection of 2 list
		#l2 is a nested list
		l=[]
		for i in l1:
			for j in l2:
				for k in j:
					if(i==k):l.append(k)
		l=self.unique(l)
		return l

	def rock(self,index,sm=False):
		p=index
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		R=[]
		for i in range(8-co):
			if not sm:
				if t_p[p][1]==t_p[p+8*(i+1)][1]:
					break
			
			if t_p[p+8*(i+1)][1]!="null":
				R.append(p+8*(i+1))
				break
			else:
				R.append(p+8*(i+1))
		L=[]
		for i in range(co-1):
			if not sm:
				if t_p[p][1]==t_p[p-8*(i+1)][1]:
					break
			
			if t_p[p-8*(i+1)][1]!="null":
				L.append(p-8*(1+i))
				break
			else:
				L.append(p-8*(1+i))
		U=[]
		for i in range(ro-1):
			if not sm:
				if (t_p[p][1]==t_p[p-i-1][1]):
					break
			if t_p[p-i-1][1]!="null":
				U.append(p-i-1)
				break
			else:
				U.append(p-i-1)
		D=[]
		for i in range(8-ro):
			if not sm:
				if t_p[p][1]==t_p[p+i+1][1]:
					break
			
			if t_p[p+i+1][1]!="null":
				D.append(p+i+1)
				break
			else:
				D.append(p+i+1)


		return [R,U,L,D]
	def clr(self,R):
		for i in R:
			button[i].config(bg=highlight)
	def rclr(self,R):
		for i in R:
			button[i].config(bg=t_p[i][4])
	def srch(self,v):
		for i in var:
			for j in i:
				if v==j:
					return True	
		return False
	def elephant(self,index,sm=False):
		p=index
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		ps=t_p[p][0]
		R=[]
		for i in range(8-co-self.error_m("R",ro,co)):
			if not sm:
				if t_p[p][1]==t_p[p+7*(i+1)][1]:
					break
		
			if t_p[p+7*(i+1)][1]!="null":
				R.append(p+7*(i+1))
				break
			else:
				R.append(p+7*(i+1))
		L=[]
		for i in range(co-1+self.error_m("L",ro,co)):
			if not sm:
				if t_p[p][1]==t_p[p-7*(i+1)][1]:
					break
			if t_p[p-7*(i+1)][1]!="null":
				L.append(p-7*(i+1))
				break
			else:
				L.append(p-7*(i+1))
	
		U=[]
		for i in range(self.error_m("U",ro,co)):
			if i!=0:
				if not sm:
					if t_p[p][1]==t_p[p-9*i][1]:
						break
				if t_p[p-9*i][1]!="null":
					U.append(p-9*i)
					break
				else:
					U.append(p-9*i)
		D=[]
		for i in range(9-ro-self.error_m("D",ro,co)):
			if i!=0:
				if not sm:
					if t_p[p][1]==t_p[p+9*i][1]:
						break
				if t_p[p+9*i][1]!="null":
					D.append(p+9*i)
					break
				else:
					D.append(p+9*i)
		return [R,U,L,D]
	def error_m(self,m,ro,co):
		if m=="R":
			if(ro+co)<9:
				return 9-(co+ro)
			else:
				return 0
		elif m=="L":
			if (ro+co)<9:return 0
			else:return 9-(co+ro)
		elif m=="U":
			if ro<=co:
				return ro
			else:
				return co
		elif m=="D":
			if ro<co:
				return co-ro
			else:
				return 0
	def horse(self,index,sm=False):
		p=index
		p=p
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		ps=t_p[p][0]
		U=[p+10,p-6,p-10,p+6,p+15,p+17,p-17,p-15]
		for i in range(6):
			if p==8*i+6:U.pop(0)
		
		for i in range(8):
			if p==8*i+7:
				U.pop(7)
				U.pop(5)
				U.pop(0)
			elif p==8*i+1:U.pop(2)
			elif p==8*i:
				U.pop(6)
				U.pop(4)
				U.pop(2)
		n_0=[]
		o=0
		for i in U:
			if (i>=0)&(i<64):n_0.append(i)
		n_1=[]
		for i in n_0:
			if not sm:
				if (t_p[i][1]!=team)|(t_p[i][1]=="null"):n_1.append(i)
			else:n_1.append(i)
		n_0=[]
		for i in n_1:
			if (ro!=t_p[i][2])&(co!=t_p[i][3]):
				n_0.append(i)
		U=n_0	
		return [U]	
	def queen(self,index,sm=False):
		p=index
		p=p
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		var=self.rock(index,sm)
		var1=self.elephant(index,sm)
		var2=[]
		for i in range(4):
			var2.append(var[i]+var1[i])
		return var2
	def soldier(self,index,sm=False):
		p=index
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		R=[]

		
		def firstmv(R):
			try:
				if t_p[p][5]==1:
					if team=="White":
						if t_p[p-2][1]!="null":pass
						elif t_p[p-1][1]=="null":R.append(p-2)
					elif team=="Black":
						if t_p[p+2][1]!="null":pass
						elif t_p[p+1][1]=="null":R.append(p+2)
			except:pass

		if team=="White":
			if not sm:
				firstmv(R)
				if (p-1>=0)&(p-1<64):
					if t_p[p-1][1]=="null":
						R.append(p-1)
			if (p+7>=0)&(p+7<64):
				if not sm:
					if t_p[p+7][1]=="Black":
						R.append(p+7)
				else:R.append(p+7)
			if (p-9>=0)&(p-9<64):
				if not sm:
					if t_p[p-9][1]=="Black":
						R.append(p-9)
				else:R.append(p-9)

		elif team=="Black":
			if not sm:
				firstmv(R)
				if (p+1>=0)&(p+1<64):
					if t_p[p+1][1]=="null":
						R.append(p+1)
			if (p-7>=0)&(p-7<64):
				if not sm:
					if t_p[p-7][1]=="White":
						R.append(p-7)
				else:R.append(p-7)
			if (p+9>=0)&(p+9<64):
				if not sm:
					if t_p[p+9][1]=="White":
						R.append(p+9)
				else:R.append(p+9)


	
		return [R]
	def king(self,index,sm=False):
		p=index
		team=t_p[p][1]
		position=(t_p[p][0])
		ro=t_p[p][2]
		co=t_p[p][3]
		if p==0:
			R=[p+1,p+8,p+9]
		elif p==56:R=[p-8,p+1,p-7]
		elif p==7:R=[p+8,p+7,p-1]
		elif p==63:R=[p-8,p-9,p-1]
		else:
			for i in range(8):
				if p==8*i+7:
					R=[p+7,p+8,p-8,p-9,p-1]
					break
				elif p==8*i:
					R=[p+1,p+9,p-8,p+8,p-7]
					break
				elif p==i:
					R=[p+8,p-1,p+1,p+7,p+9]
					break
				elif p==i+56:
					R=[p+1,p-1,p-8,p-7,p-9]
					break
				else:R=[p+1,p-1,p+7,p-7,p+8,p-8,p+9,p-9]

		def recur(R):
			k=0
			for i in R:
				if t_p[i][1]==team:
					R.pop(k)
					recur(R)
				else:k+=1
		if not sm:recur(R)
		return [R]	
	def selwin(self,t,p):
		global pteam,Turn,selected,selwin
		selwin=True
		newwin=Tk()
		def close():pass
		def sel(a):
			global Turn,selwin,undo
			del selwin
			undo.insert(0,[p,p_id,[t_p[p_id][0],t_p[p_id][1],[t_p[p][0],t_p[p][1]]]])
			
			t_p[p][0]=a
			t_p[p][1]=t
			t_p[p][6]=self.imager(Turn,a)
			button[p].config(image=self.imager(Turn,a))
			t_p[p_id][0]="empty"
			t_p[p_id][1]="null"
			if Turn=="White":Turn="Black"
			elif Turn=="Black":Turn="White"
			t_p[p_id][6]=self.imager(t_p[p_id][4],"empty")
			button[p_id].config(image=self.imager(t_p[p_id][4],"empty"))
			newwin.destroy()

		Label(newwin,text="select a position").pack()
		Button(newwin,text="Elephant",command=lambda:sel("elephant")).pack()
		Button(newwin,text="Horse",command=lambda:sel("horse")).pack()
		Button(newwin,text="rock",command=lambda:sel("rock")).pack()
		Button(newwin,text="queen",command=lambda:sel("queen")).pack()
		newwin.protocol("WM_DELETE_WINDOW",close)
		newwin.mainloop()
	def loadimage(self,iconpack):
		global pack
		pack=iconpack
		if pack==1:k="Key/"
		elif pack==2:k="Key1/"
		global Bempty,Wempty,Bsoldier,Wsoldier,Bking,Wking,Bqueen,Wqueen,Brock,Wrock,Welephant,Belephant,Bhorse,Whorse		
		Brock =PhotoImage(file=resource(k+"Brock.png"))		
		Wking =PhotoImage(file=resource(k+"Wking.png"))
		Bking =PhotoImage(file=resource(k+"Bking.png"))
		Wrock =PhotoImage(file=resource(k+"Wrock.png"))
		Bsoldier =PhotoImage(file=resource(k+"Bsoldier.png"))
		Wsoldier =PhotoImage(file=resource(k+"Wsoldier.png"))
		Bqueen =PhotoImage(file=resource(k+"Bqueen.png"))
		Wqueen =PhotoImage(file=resource(k+"Wqueen.png"))
		Bhorse=PhotoImage(file=resource(k+"Bhorse.png"))
		Whorse=PhotoImage(file=resource(k+"Whorse.png"))	
		Belephant=PhotoImage(file=resource(k+"Belephant.png"))
		Welephant=PhotoImage(file=resource(k+"Welephant.png"))
		Wempty=PhotoImage(file=resource(k+"Wempty.png"))
		Bempty=PhotoImage(file=resource(k+"Bempty.png"))

	def imager(self,t,position):

		global clr,Bempty,Wempty,Bsoldier,Wsoldier,Bking,Wking,Bqueen,Wqueen,Brock,Wrock,Welephant,Belephant,Bhorse,Whorse		
		if t=="Black":
			if position=="soldier":return Bsoldier
			elif position=="king":return Bking
			elif position=="queen":return Bqueen
			elif position=="horse":return Bhorse
			elif position=="elephant":return Belephant
			elif position=="rock":return Brock
			else:return Bempty
		elif t=="White":
			if position=="soldier":return Wsoldier
			elif position=="king":return Wking
			elif position=="queen":return Wqueen
			elif position=="horse":return Whorse
			elif position=="elephant":return Welephant
			elif position=="rock":return Wrock
			else:return Wempty
		else:
			if clr=="Black":return Bempty
			else:return Wempty

	def pow(self,o,index,mode="",sm=False):
		va=[[]]
		if o=="rock":va=self.rock(index,sm)
		elif o=="horse":va=self.horse(index,sm)
		elif o=="elephant":va=self.elephant(index,sm)
		elif o=="queen":va=self.queen(index,sm)
		elif o=="king":va=self.king(index,sm)
		elif o=="soldier":
			va=self.soldier(index,sm)
			if mode=="real":
				try:
					if (t_p[p][5]==1)&(self.srch(p)==1):
						t_p[p][5]=0
				except:pass
		return va


	def checks(self):
		if self.check("","White")=="nolne":print(self.check("","White"))
		if self.check("","Black")=="nlone":print(self.check("","Black"))
	def check(self,mode,team):
		k=0
		for i in t_p:
			if i[0]=="empty":k+=1
			else:
				oup=self.pow(i[0],k,"check")
				for j in oup:
					for l in j:
						if team=="Black":
							if l==BKP:
								
								if mode=="ca":self.config_analysis("Black")
								if mode=="":button[BKP].config(bg="red")
								return "Black"
							else:button[BKP].config(bg=t_p[BKP][4])
						elif team=="White":
							if l==WKP:
								
								if mode=="ca":self.config_analysis("White")
								if mode=="":button[WKP].config(bg="red")
								return "White"
							else:button[WKP].config(bg=t_p[WKP][4])
				k+=1
		return "none"


	def config_analysis(self,team):
		global t_p,WKP,BKP
		vir1=[x[:] for x in t_p]
		virWKP=WKP
		virBKP=BKP
		index=-1
		newpow=[]
		for i in t_p:
			index+=1
			if(i[1]!=team):continue
			power=self.pow(t_p[index][0],index,"real")
			for j in power:
				for k in j:
					if t_p[index][0]=="king":
						if team=="White":WKP=k
						elif team=="Black":BKP=k

					t_p[k][0]=t_p[index][0]
					t_p[k][1]=t_p[index][1]
					t_p[index][0]="empty"
					t_p[index][1]="null"
					
					status=self.check("check",team)
					if(status!=team):newpow.append(k)
					t_p=[x[:] for x in vir1]
					WKP=virWKP
					BKP=virBKP
		newpow=self.unique(newpow)
		return newpow
	def config_pos(self,team,p,position):
		global t_p,WKP,BKP
		newpow=[]
		vir1=[x[:] for x in t_p]
		virWKP=WKP
		virBKP=BKP
		power=self.pow(position,p,"real")
		for i in power:
			for j in i:
				t_p[j][0]=position
				t_p[j][1]=team
				t_p[p][0]="empty"
				t_p[p][1]="null"
				if(position=="king"):
					if team=="White":WKP=j
					elif team=="Black":BKP=j
				status=self.check("check",team)
				if(status!=team):newpow.append(j)
				t_p=[x[:] for x in vir1]
				WKP=virWKP
				BKP=virBKP
		newpow=self.unique(newpow)
		return newpow
	def inv(self,team):
		if team=="White":return "Black"
		elif team=="Black":return "White"



	def undo(self):
		global undo
		def undomove(p,p_id,cut=[]):
			global Turn,BKP,WKP
				# t_p[p_id][6]=self.imager(cut[1],cut[0])
				# t_p[p_id][0]=cut[0]
				# t_p[p_id][1]=cut[1]
			if len(cut)!=3:
				button[p].config(image=t_p[p_id][6])
				t_p[p][6]=t_p[p_id][6]
				t_p[p][0]=t_p[p_id][0]
				t_p[p][1]=t_p[p_id][1]
			else:
				button[p].config(image=self.imager(cut[1],cut[0]))
				t_p[p][6]=self.imager(cut[1],cut[0])
				t_p[p][0]=cut[0]
				t_p[p][1]=cut[1]
			if t_p[p_id][0]=="king":
				if Turn=="Black":BKP=p
				elif Turn=="White":WKP=p
		
			if t_p[p_id][4]=="Black":
				button[p_id].config(image=Bempty)
				t_p[p_id][6]=Bempty
			else:
				button[p_id].config(image=Wempty)
				t_p[p_id][6]=Wempty
			if Turn=="White":Turn="Black"
			elif Turn=="Black":Turn ="White"
			t_p[p_id][0]="empty"
			t_p[p_id][1]="null"
			if len(cut)==3:
				button[p_id].config(image=self.imager(cut[2][1],cut[2][0]))
				t_p[p_id][6]=self.imager(cut[2][1],cut[2][0])
				t_p[p_id][0]=cut[2][0]
				t_p[p_id][1]=cut[2][1]

			elif cut!=[]:
				button[p_id].config(image=self.imager(cut[1],cut[0]))
				t_p[p_id][6]=self.imager(cut[1],cut[0])
				t_p[p_id][0]=cut[0]
				t_p[p_id][1]=cut[1]
			self.check("",Turn)
			self.check("",self.inv(Turn))
			

		#undo protocol [[final_position,initial_position]]

		if len(undo)==0:return ""
		if (len(undo[0])!=3):undomove(undo[0][1],undo[0][0])
		else:undomove(undo[0][1],undo[0][0],undo[0][2])
		undo.pop(0)


	def unique(self,l):
		#make the elements in a list unique
		i=0
		while i<len(l):
			k=0
			while k<len(l):
				if k==i:
					k+=1
					continue
				if l[i]==l[k]:
					l.pop(k)
					k-=2
				k+=1
			i+=1
		return l

	def curpow(self):
		global t_p,Turn
		index=-1
		range=[]
		for i in t_p:
			index+=1
			if i[1]!=Turn or i[1]=="null":continue
			power=self.pow("soldier",index,"real")
			for j in power:
				for k in j:
					range.append(k)
		range=self.unique(range)
		return range
	def our(self):
		d=self.curpow()
		global t_p,Turn
		team=Turn
		nos=[]
		index=-1
		for i in t_p:
			index+=1
			if i[1]==team or i[1]=="null":continue
			power=self.pow(t_p[index][0],index,"real",True)
			for j in power:
				for k in j:
					for l in d:
						if l==k:
							nos.append(k)
		nos=self.unique(nos)
		self.clr(nos)
	def selfmove(self):
		global t_p,WKP,BKP,Turn
		Found=False
		index=0
		while not Found:
			index+=1
			pre=randint(0,63)
			if index==60:return ""
			n_0=[]
			if t_p[pre][1]==Turn:
				power=self.pow(t_p[pre][0],pre)
				for i in power:
					for j in i:
						n_0.append(j)
				if len(n_0)!=0:
					Found=True
					
					p=n_0[randint(0,len(n_0)-1)]
					if t_p[p][0]!="empty":undo.insert(0,[p,pre,[t_p[p][0],t_p[p][1]]])
					else:undo.insert(0,[p,pre,[]])
					button[p].config(image=t_p[pre][6])
					t_p[p][6]=t_p[pre][6]
					t_p[p][0]=t_p[pre][0]
					t_p[p][1]=t_p[pre][1]
					if t_p[pre][0]=="king":
						if Turn=="Black":BKP=p
						elif Turn=="White":WKP=p
					if t_p[pre][4]=="Black":
						button[pre].config(image=Bempty)
						t_p[pre][6]=Bempty
					else:
						button[pre].config(image=Wempty)
						t_p[pre][6]=Wempty
					Turn=self.inv(Turn)
					t_p[pre][0]="empty"
					t_p[pre][1]="null"










