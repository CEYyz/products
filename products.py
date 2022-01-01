products = []
while True:
	name = input('pls type product name: ')
	if name == 'q':
		break
	price = input('pls type product price: ')
	p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price)
	products.append(p)

for pro in products:
	print(pro[0], '的價格是', p[1])

