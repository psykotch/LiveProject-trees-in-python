# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:07:42 2022

@author: francois.machuron
"""

class NaryNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, value):
        self.children.append(NaryNode(value))
    def __str__(self):
        result = f'{self.value}:'
        for child in self.children:
            result += f' {child.value}'
        return result