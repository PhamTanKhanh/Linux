print("Nhap so a: ")
a = input()
print("Nhap so b: ")
b = input()
print("Nhap phep toan (+,-,*,/,%,**): ")
pt = raw_input()
if(pt == "+"):
	print("a+b=",a+b)
elif(pt == "-"):
	print("a-b=",a-b)
elif(pt == "*"):
	print("a*b=",a*b)
elif(pt == "/"):
	print("a/b=",a/b)
elif(pt == "%"):
	print("a%b=",a%b)
elif(pt == "**"):
	print("a^b=",a^b)
elif(pt !="+"):
	print("Nhap sai phep toan")
