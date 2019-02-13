print ("******************************************************")
print ('*PROGRAM UNTUK MEMENTUKAN BILANGAN TERBESAR*')
print ('******************************************************')

def pengulangan():
	print ('Masukan 3 Bilangan yang diinginkan')
	a=int(input('bilangan1 = '))
	b=int(input('bilangan2 = '))
	c=int(input('bilangan3 = '))

	if a>b and a>c:
		if b>c:
			print (a, 'bilangan terbesar')
		else:
			print (a, 'bilangan terbesar')
	elif b>a and b>c:
		if a>c:
			print (b, 'bilangan terbesar')
		else:
			print (b, 'bilangan terbesar')
	else:
		if a>b:
			print (c, 'bilangan terbesar')
		else:
			print (c, 'bilangan terbesar')

	print (' ')
	
	print ('Ingin Mencoba Kembali? (YES/NO)')
	x=input()
	if x== 'YES':
			return pengulangan()
	if x== 'NO':		
		print('*Sekian Dan Terimakasih. VIKAR KAMIL AL RAFI TI.18.A1*')
pengulangan()
print ('******************************************************')

