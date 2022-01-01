#讀取檔案
products =[]
with open('products.csv', 'r') as f:
	for line in f:
		if '商品, 價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)


#使用者輸入
products = []
while True:
	name = input('pls type product name: ')
	if name == 'q':
		break
	price = input('pls type product price: ')
	price = int(price)
	p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price)
	products.append(p)

for pro in products:
	print(pro[0], '的價格是', pro[1])

#寫入檔案
with open('products.csv', 'w') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' +str(p[1]) + '\n')