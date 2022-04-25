class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def add_left(self, value):
        self.left_child = BinaryNode(value)
    def add_right(self, value):
        self.right_child = BinaryNode(value)
        
    def __str__(self):
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