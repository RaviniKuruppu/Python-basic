class Node:

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
        if self.data:
            if ((data[0]=='OPERATOR') and(not bracketed )):
                a=self
                self=Node(data)
                self.left=a
            elif(bracketed):
                c=self.right
                self.right=Node(data)
                self.right.left=c
            elif(data[0]=='OPERAND'):
                if(self.right is None):
                    self.right=Node(data)
                else:
                    self.right.right=Node(data)      
        else:
            self.data = data       
        return self

    def evaluate(self):
        res =[]
        if self:
            res = res + Node.evaluate(self.left)
            res.append(self.data[1])
            res = res + Node.evaluate(self.right)
        '''if self:
            Node.evaluate(self.left)
            print(self.data)
            Node.evaluate(self.right)
        return '''

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
# Get the output.
root.evaluate() 
# Should print 100






