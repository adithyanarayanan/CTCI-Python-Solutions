def generateList():
	
	n = int(raw_input('Enter number of elements: '))
	head = None

	if n > 0:
		head = Node(int(raw_input("Enter element " + str(1) + ": ")))
	else:
		print 'Number of elements must be greater than 0'
		exit()

	tail = head
	for i in xrange(n-1):
		temp = Node(int(raw_input("Enter element " + str(i+2) + ": ")))
		insertAtEnd(tail, temp)
		tail = tail.next

	return head

class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

	def __repr__(self):
		return str(self.value)

def findNodeInList(head, value):

	while head is not None:
		if head.value == value:
			return head
		head = head.next
	return head

def insertAtEnd(tail, node):
	tail.next = node
	node.prev = tail

def printList(head):
	while head is not None:
		print head
		head = head.next

def getList(head):
	linkedList = []
	while head is not None:
		linkedList.append(head.value)
		head = head.next
	return linkedList

# Returns singly linked list
def reverseList(head):
	rHead = None
	while head is not None:
		temp = Node(head.value, rHead, None)
		rHead = temp
		head = head.next
	return rHead

def isEqual(head1, head2):
	while head1 is not None and head2 is not None:
		if head1.value != head2.value:
			return False
		head1 = head1.next
		head2 = head2.next
	return head1 is None and head2 is None

def getKthNode(head, k):
	while k > 0 and head is not None:
		k -= 1
		head = head.next

	return head
	