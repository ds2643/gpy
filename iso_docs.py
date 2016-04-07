#The IsoGraph class provides an alternate interface, of my own creation,
# for creating graph instances from NetworkX. 
#My ambition is to liberate Synthetic from dependancies on NetworkX. 
#However, this library is far from mature.

#The following tests are intended to demonstrate how this interface may be used.
#A set of dummy data shapes instances of the graph for each combination of parameters
#(e.g., weighted, directed, etc?).

#results are shown as comments for clarity.

# instantiation of graph requires client to indicate if graph is weighted and directed.
# regardless, internal representation is the same-- an adj matrix
# here, a directed unweighted graph is instantiated 
import isomer as g
DUG = g.IsoGraph(False,True)

# for this directed unwieghted graph, dummy nodes and edges added peicemeal
DUG.addNode('a')
DUG.addNode('b')
DUG.addNode('c')
DUG.addNode('d')
# remember to specify edge weights for weighted graphs! unweighted represented as boolean values
DUG.specEdge('a','b',1)
DUG.specEdge('a','c',1)
DUG.specEdge('a','d',1)
DUG.specEdge('b','c',1)

#internal matrix representations using graph.audit() method:
''' directed unweighted '''
#[[False  True  True  True]
# [False False  True False]
# [False False False False]
# [False False False False]]
''' directed weighted: '''
#[[     0.     10.    100.   1000.]
# [     0.      0.  10000.      0.]
# [     0.      0.      0.      0.]
# [     0.      0.      0.      0.]]
''' undirected unweighted: '''
#[[False  True  True  True]
# [ True False  True False]
# [ True  True False False]
# [ True False False False]]
''' undirected weighted: '''
#[[     0.     10.    100.   1000.]
# [    10.      0.  10000.      0.]
# [   100.  10000.      0.      0.]
# [  1000.      0.      0.      0.]]

# .adjList(): adjacency list-- dict holding list of neighbors for each node-key
#	\=> ideal for sparse graphs 
print str(DUG.adjList())
# directed unweighted: {'a': ['c', 'b', 'd'], 'c': [], 'b': ['c'], 'd': []}
# directed weighted: {'a': ['c', 'b', 'd'], 'c': [], 'b': ['c'], 'd': []}    #note omission of weights!
	##### oops... no weights here!
# unweighted undirected: {'a': ['c', 'b', 'd'], 'c': ['a', 'b'], 'b': ['a', 'c'], 'd': ['a']}
# wieghted undirected: {'a': ['c', 'b', 'd'], 'c': ['a', 'b'], 'b': ['a', 'c'], 'd': ['a']}

'''other methods: '''

''' standing issues '''
# weights left out of adjacency list representation
#     \=> must be addressed before conversion between two representations devised
