class employee():
    r=1.3
    def __init__(self):
        self.fname=input("enter the first name : ")
        self.lname=input("enter the last name : ")
        self.empid=int(input("enter the employye id : "))
        self.pay=int(input("enter the salary : "))
    def display(self):
        print(f"Name {self.fname} {self.lname}")
        print("Employee id : ",self.empid)
        print("pay",self.pay)  
    def increase(self):
        r=1.3
        self.pay=int(self.pay*r)   
class developer(employee):
    def increase(self):
        r=1.8
        self.pay=int(self.pay*r)
class manager(employee):
    def increase(self):
        r=3.2
        self.pay=int(self.pay*r) 
print("1.Manager")
print("2.Developer")
while True:
    ch=int(input("enter the choice : "))
    if ch==1:
        print("---Manager---")
        e1=manager()
        e1.increase()
        print("-----------display----------")
        e1.display()
    elif ch==2:
        e2=manager()
        e2.increase()
        e2.display()  
    else:
        break