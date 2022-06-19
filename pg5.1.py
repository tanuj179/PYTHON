#multilevel
class student():
    def __init__(self):
        print("-------super class-----")
        self.name=str(input("enter the name : "))
        if self.name.isalpha() == True:
            print()
        else:
            print("invalid name")
            return self.name
        self.usn=int(input("enter the usn : "))
        self.age=int(input("enter the age : "))        
        
class derived1(student):
    def __init__(self):
        student.__init__(self)
        print("-------first derived class-----")
        self.sem=int(input("enter the sem : "))
        derived1.display(self)
    def display(self):
        print("NAME : ",self.name) 
        print("USN : ",self.usn)
        print("AGE : ",self.age)
        print("SEMESTER : ",self.sem)   
class derived2(derived1):
    def __init__(self):
        derived1.__init__(self)
        print("---------derived class2------")
        self.sub1=int(input("enter the marks of subject 1 : ")) 
        self.sub2=int(input("enter the marks of subject 2 : "))  
        self.sub3=int(input("enter the marks of subject 3 : "))  
        self.sub4=int(input("enter the marks of subject 4 : "))  
        self.sub5=int(input("enter the marks of subject 5 : ")) 
        derived2.per(self)  
    def per(self): 
        total=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
        print("SUBJECT 1 : ",self.sub1)
        print("SUBJECT 2 : ",self.sub2)
        print("SUBJECT 3 : ",self.sub3)
        print("SUBJECT 4 : ",self.sub4)
        print("SUBJECT 5 : ",self.sub5)
        print("Total marks : ",total)
        per = (total/250)*100
        print("PERCENTAGE : ",per)
print("1.TO enter the student DEtails")
print("2.enter the student details and calculated percentage")
print("0 exit")
while True:
    ch =int(input("enter the choice : "))
    if ch==1:
        stud=derived1()
    elif ch==2:
        stud=derived2()
    else:
        break