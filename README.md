# Synthetic
Synthetic is a graph database written for Python. Previously, NetworkX (https://networkx.github.io/) provided the graph interface upon which this project was based. However, I am in the process of replacing NetworkX with my own graph system called amg, not for any shortcoming of NX, but because this project is intended as a learning exercise.

# Contents
synthetic.py:
isomer.py

# tests/documentation:
synthetic_test.py: incomplete, a work in progress (april 6 2016)
isomer_test.py (demonstrates internal representation as adj matrix for my graph module)
isomer_docs.py: my attempt at documenting the isomer graph interface through testing... content from isomer_test.py

# Goals
1. Set baseline for working prototype
2. Write well documented tests, experimenting with the idea

# Dependancies
Numpy, NetworkX, MatPlotLib
