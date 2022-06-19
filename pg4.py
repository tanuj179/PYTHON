class op():
    def __init__(self):
        self.l1=[]
    def get(self):
        n=int(input("enter the size of list "))
        for i in range(0,n):
            self.l1.append(int(input(f"\n enter the elemet {i+1} : ")))
        print("list is ",self.l1)
    def __add__(self,other):
        new_list=[]
        for i in range(0,len(self.l1)):
            new_list.append(self.l1[i]+other.l1[i])
        print("the new list after addition ",new_list)
    def __sub__(self,other):
        new_list=[]
        for i in range(0,len(self.l1)):
            new_list.append(self.l1[i]-other.l1[i])
        print("the new list after addition ",new_list)
    def __mul__(self,other):
        new_list=[]
        for i in range(0,len(self.l1)):
            new_list.append(self.l1[i]*other.l1[i])
        print("the new list after addition ",new_list)
    def __floordiv__(self,other):
        new_list=[]
        for i in range(0,len(self.l1)):
            new_list.append(self.l1[i]//other.l1[i])
        print("the new list after addition ",new_list)