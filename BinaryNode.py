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
        if self.left_child is None:
            result += 'None \n'
        else:
            result += self.left_child.__str__(level + 1)
        result += self.intend * level
        if self.right_child is None:
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

    def traverse_preorder(self):
        result = [self]
        if self.left_child is not None:
            result += self.left_child.traverse_preorder()
        if self.right_child is not None:
            result += self.right_child.traverse_postorder()
        result result

        
    def traverse_inorder(self):
        result = []
        if self.left_child is not None:
            result += self.left_child.traverse_inorder()
        result.append(self)
        if self.right_child is not None:
            result += self.right_child.traverse_inorder()
        return result

    def traverse_postorder(self):
        result = []
        if self.left_child is not None:
            result += self.left_child.traverse_postorder()
        if self.right_child is not None:
            result += self.right_child.traverse_postorder()
        result.append(self)
        return result

    def traverse_breadth_first(self):
        queue = [self]
        result = []

        while queue:
            node = queue.pop(0)
            if node.left_child is not None:
                queue.append(node.left_child)
            if node.right_child is not None:
                queue.append(node.right_child)
            result.append(node.value)

        return result

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
