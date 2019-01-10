from Node import Node
class Graph:
	def __init__(self):
		self.vert_dict = {}
		self.num_vertices = 0

	def __iter__(self):
		return iter(self.vert_dict.values())

	def add_node(self, node):
		self.num_vertices = self.num_vertices + 1
		new_node = Node(node)
		self.vert_dict[node] = new_node
		return new_node

	def get_node(self, n):
		if n in self.vert_dict:
			return self.vert_dict[n]
		else:
			return None

	def add_edge(self, frm, to, weight):
		if frm not in self.vert_dict:
			self.add_node(frm)
		if to not in self.vert_dict:
			self.add_node(to)

		self.vert_dict[frm].add_neighbor(self.vert_dict[to], weight)
		self.vert_dict[to].add_neighbor(self.vert_dict[frm], weight)

	def get_vertices(self):
		return self.vert_dict.keys()