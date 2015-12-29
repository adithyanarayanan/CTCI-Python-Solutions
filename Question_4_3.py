# Will be using a tree generated by 4.2 to test our code
from Question_4_2 import *

# Will be returning a list of lists
def listOfDepths(root):
	if root is None:
		return []
	array = []
	array.append([])
	array[0].append(root)

	level = 0
	while True:
		if not array[level]: # Checking if current level is empty
			break
		array.append([])
		for node in array[level]:
			if node._left is not None:
				array[level+1].append(node._left)
			if node._right is not None:
				array[level+1].append(node._right)
		level += 1
	return array

if __name__ == '__main__':
	n = int(raw_input('Enter length of array: '))
	array = empty((n))

	for i in xrange(n):
		array[i] = int(raw_input("Enter element " + str(i+1) + ": "))

	root = minTree(array)
	answer = listOfDepths(root)

	for l in answer:
		print l




