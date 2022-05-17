import BinaryNode as BinaryNode
import NaryNode as NaryNode

root = BinaryNode("A")
root.add_left("B")
root.add_left("C")
root.left_child.add_left("D")

new = BinaryNode.find_node(root, "D")
print(new.value)

nary = NaryNode.NaryNode("A")
nary.add_child("B")
nary.add_child("C")
nary.add_child("D")
nary.children[0].add_child("E")

new = NaryNode.find_node(nary, "F")
print(new)
