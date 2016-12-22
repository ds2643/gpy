# GPY
gpy is a graph utility written for Python. Previously, NetworkX (https://networkx.github.io/) provided the graph interface upon which this project was based. However, I am in the process of replacing NetworkX with my own graph system called amg, not for any shortcoming of NX, but because this project is intended as a learning exercise.

# Contents
main.py, the module from which the project runs
amg.py, a graph library that uses adjacency matricies (numpy) to represent graphs

# tests/documentation:
synthetic_test.py: retired testing file
isomer_test.py: retired demonstration of internal representation as adj matrix for amg precursor
isomer_docs.py: prior attempt at documenting the isomer graph interface through testing

# Goals
1. implement an elegant method for saving and loading node sets
2. periodically add algorithmic support for trees and graphs (e.g., breadth first search, minimum spanning tree)
3. extend algorithmic support to multiple graphs in a node space

# Dependencies
Numpy, NetworkX (void), MatPlotLib
