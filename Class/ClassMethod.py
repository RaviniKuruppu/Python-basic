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
    
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay=emp_str.split()
        return cls(first,last,pay)
    
emp_str="john smith 90000"
emp_str1="Bob Ferroro 50000"
emp_str2="pin lubric 60000"

new_emp=Employee.from_string(emp_str)
new_emp1=Employee.from_string(emp_str1)
new_emp2=Employee.from_string(emp_str2)

print(new_emp.fullname())
