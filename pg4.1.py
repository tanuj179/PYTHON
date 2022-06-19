#magics method
from pg4 import *
a=op()
b=op()
a.get()
b.get()
while True:
    print("1 for addition")
    print("2 for subtratcion")
    print("3 for multiplictaion")
    print("4 for floor division")
    ch = int(input("enter your choice"))
    if ch==1:
        a+b
    elif ch==2:
        a-b
    elif ch==3:
        a*b
    elif ch==4:
        a//b
    else:
        quit()