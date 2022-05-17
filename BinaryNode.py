class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.intend = "  "

    def add_left(self, value):
        self.left_child = BinaryNode(value)

    def add_right(self, value):
        self.right_child = BinaryNode(value)

    def __str__(self, level=0):
        result = f'{self.value}: \n'
        level += 1
        result += self.intend * level
        if (self.left_child == None):
            result += 'None \n'
        else:
            result += self.left_child.__str__(level + 1)
        result += self.intend * level
        if (self.right_child == None):
            result += 'None \n'
        else:
            result += self.right_child.__str__(level + 1)
        return result

        """
        result = f'{self.value}:'
        if (self.left_child == None):
            result += ' None'
        else:
            result += f' {self.left_child.value}'

        if (self.right_child == None):
            result += ' None'
        else:
            result += f' {self.right_child.value}'
        return result 
        """


def find_node(node, value):
    if node is None:
        return None
    if node.value == value:
        return node
    result = find_node(node.left_child, value)
    if result is not None:
        return result
    result = find_node(node.right_child, value)
    return result
