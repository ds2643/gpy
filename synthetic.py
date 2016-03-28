'''
standing issue:
1. named referrences in entrySpace
2. killEntry doesn't work yet
'''

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

#def grab_name(obj):
	#''' hacky way to grab object referrences '''
	#import gc
	#return str(gc.get_referrers(obj)[0])[-12:-2] #output something like "0xafb07c4c"	

class EntrySpace:
	''' atomic identity. represented by graph node. '''
	#necessary to sync nodes across several graphs
	def __init__(self,entries):
		#self.entries = defaultdict(lambda: []).fromkeys(entries)
		self.entries = dict().fromkeys(entries)
	def showFields(self, entry=''):
		''' shows all fields of which this entry is a member'''
		if entry != '':
			assert self.entries.__contains__(entry), str(entry) + " not a defined entry."
			ass_fields = self.entries[entry]
		else:
			ass_fields = [(str(entry), self.entries[entry]) for entry in self.entries]
		return ass_fields

class Field:
	''' client-side field interface'''
	def __init__(self, entrySpace, directed=0):
		''' defaults to symmetric relations... directed = 1 for assymetric relations '''
		#super(Field, self)
		#add python3 support super().__init__()
		if directed:
			self.interface = nx.DiGraph()
		else:
			self.interface = nx.Graph()
		self.entrySpace = entrySpace
		assert isinstance(self.entrySpace,EntrySpace), "offer a proper entry space as second arg!"
	def entrySpace(self):
		'''which entry space?'''
		return self.entryspace.entries
	def revealEntries(self):
		''' returns iterator over all entries in the field '''
		# safe for digraphs and undigraphs
		return self.interface.__iter__()
	def howManyEntries(self):
		''' returns count of entries '''
		#return self.interface.number_of_nodes()
		return self.interface.order()
	def addEntry(self,entry):
		''' add entry to field '''
		self.interface.add_node(entry) 
		if self.entrySpace.entries.has_key(entry):
			if self.entrySpace.entries[entry] == None:
				self.entrySpace.entries[entry] = [str(self)] #fix to add name of referrenced field instance
			elif not self.entrySpace.entries[entry].__contains__(str(self)):
				self.entrySpace.entries[entry].append(str(self))
		elif not self.entrySpace.entries.has_key(entry):
			self.entrySpace.entries[entry] = [str(self)]
	def allEntries2(self):
		''' return list of all entries in field '''
		return self.interface.nodes()
	def isMember(self,entry):
		''' returns bool indicating if entry is a member of this field '''
		return entry in self.interface
		#self.interface.has_node(entry)
	def addLink(self, node1, node2):
		assert self.isMember(node1) and self.isMember(node2), "please add nodes to field first!"
		self.interface.add_edge(node1, node2)
	def neighbors(self,entry):
		''' return list of neighbors of given entry'''
		return self.interface.neighbors(entry)
	def killEntry(self,entry):
		''' delete entry from this field'''
		assert self.isMember(entry), "you cannot remove an entry from this field that is not a member!"
		self.interface.remove_node(entry)

	def killEntry(self,entry):
		''' deletes collection of multiple entries'''
		self.interface.remove_nodes_from(entry)
	def countRelations(self):
		''' returns int number of connections specified for this field'''
		return self.interface.size()
	def prune(self):
		''' kill all defined relationships between entries'''
		self.interface.clear()
	def clone(self):
		''' create copy of this field '''
		self.interface.copy()

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
	specialMarkers = {"$e","$f"}
	#break this into a f => what did I mean here? just collapse repeated material into single fx
	rawEntries = []
	for entryLine in [line.startswith("$e") for line in rawContent]:
		rawEntries.append(entryLine[2:]) #delete prepending "$e"
	rawFields = []
	for fieldLine in [line.startswith("$f") for line in rawContent]:
		rawFields.append(fieldLine[2:]) #deleted prepending "$f", but "_tag_" still an issue for processing
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

def audit(fields, saveName=""):
	''' draws all current graphs, overlapping '''
	for field in data.fields: #hopefully this works
		nx.draw(field.interface) #test
	plt.show()
	if saveName!="": #use better screening criteria for valid filename
		plt.saveFig(str(saveName) + ".png")
		print "visual representation saved as: " + str(saveName)

