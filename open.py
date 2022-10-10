class Alphabets:
	def heart(self,name):
		grid = [[' ', ' ', ' ', ' ', ' ', ' '],
		        [' ', 'O', 'O', ' ', ' ', ' '],
		        ['O', 'O', 'O', 'O', ' ', ' '],
		        ['O', 'O', 'O', 'O', 'O', ' '],
		        [' ', 'O', 'O', 'O', 'O', 'O'],
		        ['O', 'O', 'O', 'O', 'O', ' '],
		        ['O', 'O', 'O', 'O', ' ', ' '],
		        [' ', 'O', 'O', ' ', ' ', ' '],
		        [' ', ' ', ' ', ' ', ' ', ' ']]
		import numpy as np
		a= np.array(grid)
		for i in a.T:
		    for j in i:
		        print(j,end= " ")
		    print("")
	def a(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (((column==1 or column==5) and row!=0) or ((row ==0 or row==3) and (column>1 and column<5))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def b(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (column==1 or ((row==0 or row==3 or row==6) and (column<5 and column>1)) or (column==5 and (row!=0 and row!=3 and row!=6))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def c(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (((column==1) and row!=0 and row!=6 ) or ((row ==0 or row==6 or row==3 and (row!=3 and column!=6)) and (column>1 and column<5))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def d(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (column==1 or ((row == 0 or row==6) and (column > 1 and column<5)) or (column == 5 and row != 0 and row !=6)):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str);
	def e(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (column==1 or ((row==0 or row==3 or row==6) and (column<5 and column>1)) ):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def f(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (column==1 or ((row==0 or row==3 ) and (column<5 and column>1)) ):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def g(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1 and row!=0 and row!=6) or ((row ==0 or row==6)and column>1 and column<5) or (row==3 and column>2 and column<6) or (column==5 and row!=0 and row!=2 and row!=6)):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def h(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1 or column==5) or (row==3 and (column>1 and column<6))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def i(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==3) or ((row==0 or row==6) and (column!=0 and column!=6)) ):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def j(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==3) or ((row==0) and (column!=0 and column!=6)) or (row==6 and (column>0 and column<4))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def k(self,name):
		i=0
		j=5
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1) or (row==column+1 and column>1 )):
					result_str=result_str+"*"
				elif ((row==i and column==j) and column>0):
					result_str=result_str+"*"
					i=i+1
					j=j-1
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def l(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1) or (row==6 and (column!=0 and column!=6))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def m(self,name):
		i=1
		j=4
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==0 or column==6) or (row==column and (column>0 and column<4)) ):
					result_str=result_str+"*"
				elif ((row==i and column==j+1) and column>2):
					result_str=result_str+"*"
					i=i+1
					j=j-1
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def n(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==0 or column==6)  or (row==column and (column>0 and column<6))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def o(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (((column==1 or column==5) and row!=0 and row!=6 ) or ((row ==0 or row==6 or row==3 and (row!=3 and column!=6)) and (column>1 and column<5))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def p(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1 ) or ((row ==0 or row==3) and ((column>1 and column<6))) or ((column==5) and (row>0 and row<4))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def q(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==5 ) or ((row ==0 or row==3) and ((column>0 and column<6))) or ((column==1) and (row>0 and row<4))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def r(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1) or (row==column+1 and column>1 ) or ((row ==0 or row==3) and ((column>0 and column<5))) or ((column==5) and (row>0 and row<3))):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def s(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ( (column==1 and row<4) or ((row==0 or row==3) and (column>0 and column<6)) or (column==5 and row>2) or (column>0 and column<6) and (row==6) ):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def t(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (row==0 or column==3 ):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def u(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((row==6 and column!=0 and column!=6 )or column==1 or column==5):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def v(self,name):
		i=4
		j=4
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1 and row<4 or column==5 and row<4) or (row==4 and column==2) ):
					result_str=result_str+"*"
				elif ((row==i and column==j) and column>2):
					result_str=result_str+"*"
					i=i+1
					j=j-1
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def w(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==1 or column==5 ) or ((row==5) and (column>1 and column<5 and column!=3 )) or (row==4 and column==3)):
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def x(self,name):
		i=0
		j=6
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((row==column-1 and column>0 )):
					result_str=result_str+"*"
				elif ((row==i and column==j) and column>0):
					result_str=result_str+"*"
					i=i+1
					j=j-1
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str,);
	def y(self,name):
		i=0
		j=6
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ((column==3 and row>2) or (row==column and column>=0 and column<3 )):
					result_str=result_str+"*"
				elif ((row==i and column==j) and column>2):
					result_str=result_str+"*"
					i=i+1
					j=j-1
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str);
	def z(self,name):
		i=1
		j=5
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if (row==0 or row==6):
					result_str=result_str+"*"
				elif ((row==i and column==j) and column>0):
					result_str=result_str+"*"
					i=i+1
					j=j-1
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str, end = "");
	def space(self,name):
		result_str="";
		for row in range(0,7):
			for column in range(0,7):
				if ():
					result_str=result_str+"*"
				else:
					result_str=result_str+" "
			result_str=result_str+"\n"
		print(result_str, end= "");
while True:
	aa=str(input("enter your name : "))
	for bb in aa:
		c=Alphabets()
		if (bb=="a"or bb=="A"):
			c.a(bb)
		elif(bb=="b"or bb=="B"):
			c.b(bb)
		elif(bb=="c"or bb=="C"):
			c.c(bb)
		elif(bb=="d"or bb=="D"):
			c.d(bb)
		elif(bb=="e"or bb=="E"):
			c.e(bb)
		elif(bb=="f"or bb=="F"):
			c.f(bb)
		elif(bb=="g"or bb=="G"):
			c.g(bb)
		elif(bb=="h"or bb=="H"):
			c.h(bb)
		elif(bb=="i"or bb=="I"):
			c.i(bb)
		elif(bb=="j"or bb=="J"):
			c.j(bb)
		elif(bb=="k"or bb=="K"):
			c.k(bb)
		elif(bb=="l"or bb=="L"):
			c.l(bb)
		elif(bb=="m"or bb=="M"):
			c.m(bb)
		elif(bb=="n"or bb=="N"):
			c.n(bb)
		elif(bb=="o"or bb=="O"):
			c.o(bb)
		elif(bb=="p"or bb=="P"):
			c.p(bb)
		elif(bb=="q"or bb=="Q"):
			c.q(bb)
		elif(bb=="r"or bb=="R"):
			c.r(bb)
		elif(bb=="s"or bb=="S"):
			c.s(bb)
		elif(bb=="t"or bb=="T"):
			c.t(bb)
		elif(bb=="u"or bb=="U"):
			c.u(bb)
		elif(bb=="v"or bb=="V"):
			c.v(bb)
		elif(bb=="w"or bb=="W"):
			c.w(bb)
		elif(bb=="x"or bb=="X"):
			c.x(bb)
		elif(bb=="y"or bb=="Y"):
			c.y(bb)
		elif(bb=="z"or bb=="Z"):
			c.z(bb)
		elif(bb==" "):
			c.space(bb)	
		elif(bb=="3"):
			c.heart(bb)
		else:
			print("character not defined yet")

