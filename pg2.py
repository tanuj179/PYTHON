#10 operation on set
from os import popen


set1={1,2,3,4,5,6}
set2={"Tanuj","rahul"}
set3={4,5}
print("1.length of the set")
print("4 adding a set")
print("5.update set")
print("6.union of 2 set")
print("7.intersection of two set")
print("8.symmetrice differnece of 2 set")
print("9pop a element i from set")
print("10.discard the set")
print("11.clear a set")
print("12.differnece of two set")
while True:
    ch=int(input("enter the choice"))
    if ch==1:
        print(len(set1))
    elif ch==2:
       # new_Set = set((1,2,3,4,5))
       #print(new_Set)
       x = set1.add(10) 
       print(x)
    elif ch==3:
        set1.update("Tarun")
        print(set1)
    elif ch==4:
        x = set1.union(set2)
        print(x)
    elif ch==5:
        x =set1.intersection(set3)
        print(x)
    elif ch==6:
        x = set1.symmetric_difference(set3)
        print(x)
    elif ch==7:
        x = set1.pop()
        print(set1)
    elif ch==8:
        set1.discard(1)
        print(set1)
    elif ch==9:
        set2.clear()
        print(set2)
    elif ch==10:
            x=set1.difference(set3) 
            print(x) 
    elif ch==11:
        print(1 in set1)  
    else:
        quit()
        