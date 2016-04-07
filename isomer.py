import numpy as np

class IsoGraph:
	''' graph object '''
	def __init__(self, weight=False, directed=True):
		''' internal rep as adjacency matrix regardless of density'''
		self.weight = weight
		self.directed = directed
		self.room = np.float64 if (weight) else np.bool #fix this variable name
		self.adjMat = np.zeros((0,0),dtype=self.room)
		self.nodes = [] #meta data
	def addNode(self,label):
		''' insert new node into graph-- pass if label already in use '''
		if (not self.nodes.__contains__(label)):
			self.nodes.append(label)
			self.adjMat = np.resize(self.adjMat,(len(self.nodes),len(self.nodes))) #not ! f
		else: pass
	def specEdge(self,x,y,value):
		''' draw a label between nodes... supports sym for undirected graphs'''
		i = self.nodes.index(x)
		j = self.nodes.index(y)
		self.adjMat[i][j] = value
		if (not self.isDirected()):
			self.adjMat[j][i] = value
	def adjList(self):
		adjList=dict()
		for i,x in enumerate(self.nodes):
			#adjList[x]=set([self.nodes[j] for j,y in enumerate(self.adjMat[i]) if y!=0])
			adjSet = set()
			for j,y in enumerate(self.adjMat[i]):
				if y!=0:
					adjSet.add(self.nodes[j])
				else: pass
			adjList[x]=list(adjSet)
		return adjList
	def adjNodes(self,node):
		''' outputs list of adjacent vertices to node '''
		return self.adjList()[node]
	def getEdge(self,x,y):
		i = self.nodes.index(x)
		j = self.nodes.index(y)
		if (self.nodes.__contains__(x) and self.nodes.__contains__(y)):
			return self.adjMat[i,j]
		else: pass
	def audit(self): #add metadata labels
		print self.adjMat #print with meta data
	def specAsAdjMat(self,matrix):
		return None
	def isWeighted(self):
		return self.weight
	def isDirected(self):
		return self.directed
	def addEdge(self,x,y,val=1):
		i = self.nodes.index(x)
		j = self.nodes.index(y)
		self.adjMat[i][j] = val
		if (not self.directed):
			self.adjMat[j][i] = val
	def delEdge(self,x,y):
		i = self.nodes.index(x)
		j = self.nodes.index(y)
		self.adjMat[i][j] = 0
		if (not isDirected()):
			self.adjMat[j][i] = 0
	def iterative_dfs(self, start, path=[]):
		''' sol'n contributed by activestate'''
		GRAPH = self.adjList() #graph as adjacency list
		q=[start] # queue, a list containing item provided as argumenet
		i = 0 # counter of backticks
		while q:	# as long as q not empty...
			v=q.pop(0)	# get rid of current list item
			if v not in path: # if v is not in list
				path=path+[v]
				q=GRAPH[v]+q
		return path
	def iterative_bfs(self, start, path=[]):
		''' sol'n contributed by activestate'''
		GRAPH = self.adjList()
		q=[start]
		while q:
			v=q.pop(0)
			if not v in path:
				path=path+[v]
				q=q+GRAPH[v]
		return path
	def isConnected(self):
		return (set(self.iterative_dfs(self.nodes[0]))==set(self.nodes))
'''
__graveyard__
def delNode(self,x):
    return None
def isCyclic(self):
    if isDirected():
        return 'directed result'
    else:
        return 'undirected result
def isTree(self):
    return not isCyclic(self) and isConnected(self)

'''