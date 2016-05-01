import amg

class NodeSet:
	def __init__(self, label):
		self.label = label
		self.graphs  = []
		self.nodeset = set()
	def __repr(self):
		return self.label
	def add_node(self,node):
		''' adds node to set of nodes shared by graphs '''
		self.nodeset.add(node)
		for graph in self.graphs:
			graph.add_node(node)
		print str(node) + " added to graphs " + " ".join([graph.name for graph in self.graphs]) + "."
	def add_graph(self,label,weight,directed):
		''' adds graph to set of graphs shared amongst nodes '''
		g = amg.Graph(label, weight, directed)
		for node in self.nodeset:
			g.add_node(node)
		self.graphs.append(g)
	def save(self, filename):
		''' save this NodeSet to a file for later use '''
		pass
