from NaryNode import *
from BinaryNode import *

root = NaryNode("A")
root.add_child("C")
root.add_child("B")
root.children[0].add_child("D")
print(root)
