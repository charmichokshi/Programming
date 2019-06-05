'''
Write a function to print ZigZag order traversal of a binary tree. 
For the below binary tree the zigzag order traversal will be 1 3 2 4 5 6 7 9 8

       1
     /  \
    2    3
   / \  / \
  4  5  6  7
 / \
8   9
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def zig_zag_traversal(root):
	# two stacks
	curr_level, next_level = list(), list()

	if root is None: 
		return

	curr_level.append(root)
	left_to_right = True

	while len(curr_level) > 0:
		curr_node = curr_level.pop(-1)
		print(str(curr_node.data)+" ")

		if left_to_right:
			if curr_node.left:
				next_level.append(curr_node.left)
			if curr_node.right:
				next_level.append(curr_node.right)
		else:
			if curr_node.right:
				next_level.append(curr_node.right)
			if curr_node.left:
				next_level.append(curr_node.left)

		if len(curr_level) == 0:
			left_to_right = not left_to_right
			curr_level, next_level = next_level, curr_level
	
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

zig_zag_traversal(root)
