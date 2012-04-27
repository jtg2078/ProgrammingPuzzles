def decimal_to_binary(n):
	n = abs(n)
	b = [0] * 32
	index = 0
	while n > 0:
		b[index] = n % 2
		n /= 2
		index += 1
	b.reverse()
	return b
	
def binary_to_2s_compliment(b):
	c = []
	b.reverse()
	start_to_flip = False
	for n in b:
		if start_to_flip == False:
			if n == 0:
				c.append(n)
			else:
				c.append(n)
				start_to_flip = True
		else:
			c.append(0 if n == 1 else 1)
	c.reverse()
	return c

def count_ones(a,b):
	sum = 0
	for i in range(a, b+1):
		b = decimal_to_binary(i)
		c = binary_to_2s_compliment(b)
		print c
		sum += (c.count(1) if i < 0  else b.count(1))
	return sum

def increament_by_one(a):
	for i in range(len(a)-1, -1, -1):
		if a[i] == 0:
			a[i] = 1
			break
		else:
			a[i] = 0

def count_ones_smart(a,b):
	binary = decimal_to_binary(a)
	number = binary if a >= 0 else binary_to_2s_compliment(binary)
	sum = number.count(1)
	i = a+1
	while i <= b:
		if i < 0:
			# in two's compliment form
			increament_by_one(number)
			sum += number.count(1)
		elif i == 0:
			# rese to all zero
			number = [0] * 32
		else:
			# normal binary form
			increament_by_one(number)
			sum += number.count(1)
		i += 1
	return sum
	
def main(file_name):
	total = 0
	index = -1
	with open(file_name, 'r') as f:
		for line in f:
			tokens = line.split()
			if index == -1:
				# this is the first line, which contains # of
				# blanaces in the input file
				total = int(tokens[0])
				index = 0
				continue
			if index >= total:
				break
			a = int(tokens[0])
			b = a
			if len(tokens) > 1:
				b = int(tokens[1])
			print count_ones_smart(a, b)
			index += 1

import fileinput
def main2():
	total = 0
	index = -1
	for line in fileinput.input():
		tokens = line.split()
		if index == -1:
			# this is the first line, which contains # of
			# blanaces in the input file
			total = int(tokens[0])
			index = 0
			continue
		if index >= total:
			break
		a = int(tokens[0])
		b = a
		if len(tokens) > 1:
			b = int(tokens[1])
		print count_ones_smart(a, b)
		index += 1
		

#main2()
#main('input01.txt')




a = -594326116
b = -242747090
#print count_ones_smart(a, b)

total = 0
for i in range(0, 33):
	a = map(str,decimal_to_binary(i))
	total += a.count('1')
	print "{0:2d}: {1} ones:{2}".format(i, ''.join(a), a.count('1'))
print 'total 1s: ', total

def smart(n):
	if n == 0
	return smart(n/2) * 2




		
	