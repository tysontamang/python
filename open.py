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

aa=str(input("enter your name (only small letter): "))
for bb in aa:
	c=Alphabets()
	if (bb=="a"):
		c.a(bb)
	elif(bb=="b"):
		c.b(bb)
	elif(bb=="c"):
		c.c(bb)
	elif(bb=="d"):
		c.d(bb)
	elif(bb=="e"):
		c.e(bb)
	elif(bb=="f"):
		c.f(bb)
	elif(bb=="g"):
		c.g(bb)
	elif(bb=="h"):
		c.h(bb)
	elif(bb=="i"):
		c.i(bb)
	elif(bb=="j"):
		c.j(bb)
	elif(bb=="k"):
		c.k(bb)
	elif(bb=="l"):
		c.l(bb)
	elif(bb=="m"):
		c.m(bb)
	elif(bb=="n"):
		c.n(bb)
	elif(bb=="o"):
		c.o(bb)
	elif(bb=="p"):
		c.p(bb)
	elif(bb=="q"):
		c.q(bb)
	elif(bb=="r"):
		c.r(bb)
	elif(bb=="s"):
		c.s(bb)
	elif(bb=="t"):
		c.t(bb)
	elif(bb=="u"):
		c.u(bb)
	elif(bb=="v"):
		c.v(bb)
	elif(bb=="w"):
		c.w(bb)
	elif(bb=="x"):
		c.x(bb)
	elif(bb=="y"):
		c.y(bb)
	elif(bb=="z"):
		c.z(bb)
	elif(bb==" "):
		c.space(bb)	
	elif(bb=="3"):
		c.heart(bb)
	else:
		print("character not defined yet")