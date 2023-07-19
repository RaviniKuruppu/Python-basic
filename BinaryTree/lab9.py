class Node:
    l=""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)
    def insert(self, data, bracketed):
        if data[0] == 'OPERATOR':
            if bracketed:
                carry = self.right
                self.right = Node(data)
                self.right.left = carry
                self.status = True
            else:
                self = Node(data)
                self.left = root
        if data[0] == 'OPERAND':
            if self.status:
                self.right.right = Node(data)
                self.status = False
            else:
                self.right = Node(data) 
        return self

    def evaluate(self):
        if self.data[0] == 'OPERAND':
            return self.data[1]
        else:
            if self.data[1] == '^':
                y = self.right.evaluate() 
                x = self.left.evaluate()
                return eval(f"{x}**{y}")
            else:
                y = self.right.evaluate() 
                x = self.left.evaluate()
                return eval(f"{x}{self.data[1]}{y}")
root = Node(('OPERAND', 1))
# Form the rest of the tree by inserting data to the root node.
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), True)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
root.evaluate()