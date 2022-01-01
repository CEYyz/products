import os # oprating system
#讀取檔案
def read_file(filename):
	products =[]
	with open(filename, 'r') as f:
		for line in f:
			if '商品, 價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 使用者輸入
def user_input(products):
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
		return products

# 購買紀錄
def print_products(products):
	for pro in products:
		print(pro[0], '的價格是', pro[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('商品, 價格\n')
		for p in products:
			f.write(p[0] + ',' +str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案
		print('find this file')
		products = read_file(filename)
	else:
		print('fail...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()