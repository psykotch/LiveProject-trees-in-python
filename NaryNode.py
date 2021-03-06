# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:07:42 2022

@author: francois.machuron
"""


class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.intend = "  "

    def add_child(self, value):
        self.children.append(NaryNode(value))

    def __str__(self, level=0):
        result = (self.intend * level) + f'{self.value}: \n'
        for i in range(len(self.children)):
            result += self.children[i].__str__(level + 1)
        return result

    def traverse_preorder(self):
        result = [self]
        for child in self.children:
            result += child.traverse_preorder()
        return result

    def traverse_postorder(self):
        result = []
        for child in self.children:
            result += child.traverse_postorder()
        result.append(self)
        return result

    def traverse_breadth_first(self):
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            for child in node.children:
                queue.append(child)
            result.append(node.value)
        return result

def find_node(node, value):
    if node is None:
        return None
    if node.value == value:
        return value
    for children in node.children:
        result = find_node(children, value)
        if result is not None:
            return result
