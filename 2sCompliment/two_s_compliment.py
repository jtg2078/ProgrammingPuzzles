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
		sum += c.count(1)
	return sum
	
	
print count_ones(-2,0)

		
	