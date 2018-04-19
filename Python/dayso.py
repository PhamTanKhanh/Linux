print 'Nhap 1 so: '
n = input()

for i in range(1,n+1):
	print 'So thu: ',i
tong = 0
for i in range(1,n+1):	
	if i%2 == 0:
		tong=tong+i
print 'Tong so chan la:',tong

