import networkx as nx
import matplotlib.pyplot as plt

class Field:
	''' client-side field interface'''
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
		''' returns int number of connections specified for this field'''
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
	def showFields():
		''' shows all fields of which this entry is a member'''
	def joinField(field): #allow for variable arguments
		''' add to field '''
		if self.name in field:
			pass
		else:
			field.interface.add_node(str(name))
		#if field.addEntry(self)
	def revealDegree(self,field):
	''' ? '''
		return field.interface.degree(name)

#list of all instances currently open of field/entry

def write(data): #how is this data ag'd?
	'''write current data to some file as adjacency lists'''
	fileName = raw_input("how should we name the database file?") + ".synth"
	f = open(filename,'w')
	assert type(data.entries)
	entryTag = "$e" + str(data.entries)
	f.write(entryTag)
	for field in data.fields:	 
		for fi in field.interface.adjacency_iter():
			lineToEnter = "$f_" + field.tag + "_" + fi 
			f.write(lineToEnter)
		f.write("\n")
	f.close()	

def read(filename):
	''' read from .synth file '''
	assert filename[-3:] == ".synth", "not a valid synthetic database file!"
	fileHandle = open(filename,'r').read()
	rawContent = []
	for line in fileHandle:
		rawContent.append(line)
	specialMarkers = {$f,$E}
	rawFields = []
	#break this into a f => what did I mean here?
	for fieldLine in [line.startswith("$f") for line in rawContent]:
		rawFields.append(fieldLine[2:]) #deleted prepending "$f", but "_tag_" still an issue for processing 
	fileHandle.close()
	rawEntries = []
    for entryLine in [line.startswith("$e") for line in rawContent]:
        rawEntries.append() #delete prepending "$e" 
    fileHandle.close()
	fsToRuntime()
	esToRuntime()

def fsToRuntime(listFields):
	''' scaffolding for converting field representation from file to runtime object '''
	for field in listFields:
		print field

def esToRuntime(listEntries):
	''' scaffolding for converting field representation from file to runtime object '''
	print listEntries

def audit(data.fields,saveName=""):
	''' draws all current graphs,overlapping '''
	for field in data.fields: #hopefully this works
		nx.draw(field.interface) #test
	plt.show()
	if saveName!="": #use better screening criteria for valid filename
		plt.saveFig(str(saveName) + ".png")
		print "visual representation saved as: " + str(saveName)
