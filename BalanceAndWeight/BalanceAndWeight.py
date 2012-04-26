class Balance:
	def __init__(self):
		self.index = 0
		self.processed = False
		self.weight_left = 0
		self.weight_right = 0
		self.balance_left = []
		self.balance_right = []
		self.add_to_left = 0
		self.add_to_right = 0
		self.total = 0

def balancing(list, b):
	#print 'balance index is: ',b.index
	if len(b.balance_left) > 0 and len(b.balance_right) > 0:
		# both has more
		weight1 = 0
		for n in b.balance_left:
			#weight1 += 10 # for balance weight itself
			weight1 += balancing(list, list[n])
		b.weight_left += weight1
		weight2 = 0
		for n in b.balance_right:
			#weight2 += 10 # for balance weight itself
			weight2 += balancing(list, list[n])
		b.weight_right += weight2
	elif len(b.balance_left) > 0 and len(b.balance_right) == 0:
		# left side has more
		weight = 0
		for n in b.balance_left:
			#weight += 10 # for balance weight itself
			weight += balancing(list, list[n])
		b.weight_left += weight
	elif len(b.balance_left) == 0 and len(b.balance_right) > 0:
		# right side has more
		weight = 0
		for n in b.balance_right:
			#weight += 10 # for balance weight itself
			weight += balancing(list, list[n])
		b.weight_right += weight
	# this is the base case, when both side contains 
	# no more balances so no place to go any further down
	if b.weight_left >= b.weight_right:
		b.add_to_right = b.weight_left - b.weight_right
		b.weight_right += b.add_to_right
	else:
		b.add_to_left = b.weight_right - b.weight_left
		b.weight_left += b.add_to_left
	b.total = b.weight_left + b.weight_right + 10
	#print '{0}: {1} {2} total:{3}'.format(b.index, b.add_to_left, b.add_to_right, b.total)
	b.processed = True
	return b.total

def main(file_name):
	#print 'Reading input file:', file_name
	root = None
	list = []
	total = 0
	with open(file_name, 'r') as f:
		index = -1
		for line in f:
			tokens = line.split()
			if index == -1:
				# this is the first line, which contains # of
				# blanaces in the input file
				total = int(tokens[0])
				index = 0
				continue
			# each balance occupies two lines
			if index % 2 == 0:
				b = Balance()
				b.index = index / 2
				list.append(b)
				b.weight_left = int(tokens[0])
				for i in range(1, len(tokens)):
					b.balance_left.append(int(tokens[i]))
			else:
				b = list[index / 2]
				b.weight_right = int(tokens[0])
				for i in range(1, len(tokens)):
					b.balance_right.append(int(tokens[i]))
			index += 1
	#print 'Done reading input file'
	#print 'print out input file'
	#print 'num of balance: ', total
	#for b in list:
	#	print '[{0}]: {1} {2}'.format(b.index, b.weight_left, b.balance_left)
	#	print '[{0}]: {1} {2}'.format(b.index, b.weight_right, b.balance_right)
	#print 'start to traverse through the list and balance each tree'
	for b in list:
		if b.processed == False:
			balancing(list, b)
	#print 'Done balancing the input file, print result...'
	for b in list:
		print '{0}: {1} {2}'.format(b.index, b.add_to_left, b.add_to_right)

main('input00.txt')
main('input01.txt')
	


		
		
	