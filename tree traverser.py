class Node:
	def __init__(self, val):
		self.val = val;
		self.right = None
		self.left = None

	def getValue(self):
		return self.val

	def addLeft(self, node):
		self.left = node

	def addRight(self, node):
		self.right = node

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

class NodeValPair:
	def __init__(self, node, idx):
		self.node = node
		self.index = idx

	def getNode(self):
		return self.node

	def getIndex(self):
		return self.index

def checkAndPut(root, index, d):
	if d.has_key(index):
		currList = d[index]
		currList.append(root)
		d[index] = currList
	else:
		d[index] = [root]
	return d

def printTree(root, index, d):
	d = checkAndPut(root, index, d)
	agenda = []
	if root.getLeft() != None:
		agenda.append(NodeValPair(root.getLeft(), index -1))
	if root.getRight() != None:
		agenda.append(NodeValPair(root.getRight(), index+1))
	while agenda:
		nodeToCheck = agenda.pop()
		d = checkAndPut(nodeToCheck.getNode(), nodeToCheck.getIndex(), d)
		if nodeToCheck.getNode().getLeft() != None:
			agenda.append(NodeValPair(nodeToCheck.getNode().getLeft(), nodeToCheck.getIndex() -1))
		if nodeToCheck.getNode().getRight() != None:
			agenda.append(NodeValPair(nodeToCheck.getNode().getRight(), nodeToCheck.getIndex()+1))
	return d


def actualPrint(d, initialVal):
	for key in d:
		if key < initialVal:
			initialVal = key
	prtStr = ""
	while d.has_key(initialVal):
		valList = d[initialVal]
		for element in valList:
			prtStr = prtStr + str(element.getValue()) + " "
		initialVal += 1
	print prtStr

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
a.addLeft(b)
a.addRight(c)
b.addLeft(d)
b.addRight(e)

d = {}
newD = printTree(a, 5, d)

actualPrint(newD, 10)

