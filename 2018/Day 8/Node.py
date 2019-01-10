
class Node:

	def __init__(self, value):
		self.value = value
		self.children = []

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value = value

	def getChildren(self):
		return self.children

	def setChild(self, child):
		self.children.append(child)