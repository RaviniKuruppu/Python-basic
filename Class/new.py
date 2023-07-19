class Employee(): # class named Employee is created
    
    num_of_employee=0
    raise_amount=1.04 # class variable
    
    def __init__(self,first,last,pay):
        self.fname=first
        self.lname=last
        self.pay=pay
        self.email=first+"."+"gamil.com"
        Employee.num_of_employee += 1
    
    def fullname(self):
        return self.fname+' '+self.lname 
    
    def apply_raises(self):
        self.pay=int(self.pay * self.raise_amount)  
        
emp_1=Employee("Bob","Ferroro",50000) # here init method is run automatically
emp_2=Employee("pin","lubric",60000)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print()

print(emp_1.pay)
emp_1.apply_raises()
print(emp_1.pay)
print()

Employee.raise_amount =1.05 # change the raise ammount
print(Employee.raise_amount)
print()

emp_1.raise_amount = 2.05 # only emp_1 raise amount is changed
print(emp_1.raise_amount)
print(Employee.raise_amount)
print()

print(Employee.num_of_employee)

emp_str="john smith 90000"
first, last, pay=emp_str.split()
new_emp=Employee(first,last,pay)
print("new emp="+new_emp.fullname())

emp_1.fname ="Jim"
print(emp_1.fullname())
