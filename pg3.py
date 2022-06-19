# dict ={1:"geeks",2:"anuj",3:"tanuj"}
# print(dict)
# dict ={"name":"tanuj",1:[1,2,3,4]}
# Dict={}
# print(Dict)
# Dict = dict({1:"geeks"})
# print(Dict)
# Dict ={1:"tanuj",2:"anuj",3:{1:"welcime",2:"tanuj"}}
# print(Dict)
# Dict ={}
# Dict[0]="geeks"
# Dict[1]="tanuj"
# Dict[2]=1
# print(Dict)
# Dict [2]=10
# print("updates")
# print(Dict)
# Dict ={1:"tanuj",2:{"a":"manoj"}
#        ,3:{"arun":"tanuj"}}
# print(Dict[1])
# print(Dict[2]["a"])
# print(Dict[3]["arun"])
# d =dict()
#concept of dictionry
d =dict()
class employee():
       def input(self):
              self.name=input("enter the name : ")
              self.address=input("enter the addresss : ")
              self.pan=input("enter the pan number")
              self.basic_salary=float(input("enter the slaary : "))
              self.deduct=float(input("enter the deuction"))
              self.hra=self.basic_salary*1.25
              self.da=self.basic_salary*0.25
              self.grosspay=self.basic_salary+self.hra+self.da
              self.netpay=self.grosspay-self.deduct
              self.update()
       def update(self):
              d.update({self.name:{
                     "name":self.name,
                     "address":self.address,
                     "pan":self.pan,
                     "basic_salary":self.basic_salary,
                     "dedcution":self.deduct,
                     "hra":self.hra,
                     "da":self.da,
                     "grosspay":self.grosspay,
                     "netpay":self.netpay                     
              }})
       def printe(self):
              for key in d:
                     print(key,d[key])
       def search(self,name):
              for key in d:
                     if key==name:
                            for i in d[key]:
                                   print("found")
                                   print(i,d[key][i])      
                     else:
                            print("not found")                                    
                            
em =employee()
print("1.input")      
print("2.display")
print("3.search")

while True:
       ch = int(input("enter ther choice"))
       if ch==1:
              em.input()
       if ch==2:
              em.printe()
       if ch==3:
              name=input("enter the name")
              em.search(name)
       if ch==4:
              break