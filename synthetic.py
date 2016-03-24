import networkx as nx

class Field:
	''' experimental client-side field interface'''
	def __init__(self,directed=0):
		if directed:
			self.interface = nx.DiGraph()
		else:
			self.interface = nx.Graph()
	def revealEntries(self):
		''' returns iterator over all entries in the field '''
		# safe for digraphs and undigraphs
		return self.interface.__iter__()
	def howManyEntries(self):
		''' returns count of entries '''
		return self.interface.__len__()
	def howManyEntries(self):
		''' returns count of entries '''
		#return self.interface.number_of_nodes()
		return self.interface.order()
	def addEntry(self,entry):
		''' add entry to field '''
		self.interface.add_node(entry)
	def allEntries2(self):
		''' return list of all entries in field '''
		return self.interface.nodes()
	def isMember(self,entry):
		''' returns bool indicating if entry is a member of this field '''
		return entry in self.interface
		# self.interface.has_node(entry)
	def neighbors(self,entry):
		''' return list of neighbors of given entry'''
		return self.interface.neighbors(entry)
	def killEntry(self,entry):
		''' delete entry from this field'''
		self.interface.remove_node(entry)
	def killEntry(self,entries):
		''' deletes collection of multiple entries'''
		self.interface.remove_nodes_from(entry)
	def countRelations(self):
		return self.interface.size()
	def prune(self):
		''' kill all defined relationships between entries'''
		self.interface.clear()
	def clone(self):
		''' create copy of field '''
		self.interface.copy()

class Entry:
	''' atomic identity. represented by graph node. '''
	#necessary to sync nodes across several graphs
	def __init__(self,name):
		self.name = str(name) #bad... find another way to ref safely
	def show_fields():
		''' shows all fields of which this entry is a member'''
	def join_field(field): #allow for variable arguments
		''' add to field '''
		if self.name in field:
			pass
		else:
			field.interface.add_node(str(name))
		#if field.addEntry(self)
	def revealDegree(self,field):
		return field.interface.degree(name)
