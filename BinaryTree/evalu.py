class Node:
    l=[False]
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
        Node.l.append(bracketed)
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
        
        def cal(self): 
            res = []
            if self:
                res = cal(self.left)
                res.append(self.data[1])
                res = res + cal(self.right)
            return res
        a=cal(self)
        print(a) 
        
        def sign(a):
            temp=a[0]
            for i in range(len(a)):
                if(a[i]=="-"):
                    temp=temp-a[i+1]
                    
                elif(a[i]=="+"):
                    temp=temp+a[i+1]
                    
                elif(a[i]=="*"):
                    temp=temp*a[i+1]
                   
                elif(a[i]=="^"):
                    temp=temp**a[i+1]
            #print(temp)
            return temp
        
        if(True in Node.l ):
            for x in range(len(a)):
                if (Node.l.index(True)==x):
                    a[x]=sign(a[x-1:x+2])
                    del a[x-1]
                    del a[x]
            n=sign(a)
        else:
            n=sign(a)
        
            
        return n
root = Node(('OPERAND', 1))
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)



root.get_output() 

