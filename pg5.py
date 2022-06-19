#inheeritance hierraichal
class student():
    def __init__(self):
        self.usn=int(input("enter the usn : "))
        self.name=input("enter the name : ")
        self.age=int(input("enter the age : "))            
class ugstudent(student):
    def __init__(self):
        student.__init__(self)
        self.sem=int(input("enter the sem : "))
        self.fees=int(input("enter the fees : "))
        self.stipend=int(input("enter the stipend"))
        ugstudent.display(self)
    def display(self):
        print("Name : ",self.name)
        print("usn : ",self.usn)
        print("age : ",self.age)
        print("SEM : ",self.sem)
        print("FEES : ",self.fees)
        print("Stipend : ",self.stipend)
        
class pgstudent(student):
    def __init__(self):
        student.__init__(self)
        self.sem=int(input("enter the sem : "))
        self.fees=int(input("enter the fees : "))
        self.stipend=int(input("enter the stipend"))
        pgstudent.display(self)
    def display(self):
        print("Name : ",self.name)
        print("usn : ",self.usn)
        print("age : ",self.age)
        print("SEM : ",self.sem)
        print("FEES : ",self.fees)
        print("Stipend : ",self.stipend)
        

while True:
    print("1.ugstudent")
    print("2.pgstudent")
    ch=int(input("enter the choice : "))
    if ch==1:
        ug=ugstudent()
    elif ch==2:
       pg=pgstudent()
    else:
        break