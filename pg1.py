#stirng and tuple 10 operation
from itertools import count


var1 ="Tanuj"
var2 ="Python is programming language"
print("1.concatenation")
print("2.length of string")
print("3.reversing a string")
print("4.range slicing")
print("5.upper case")
print("6.lower case")
print("7.iteratiing")
print("8.repetation")
print("9.split")
print("10.count")
print("11.start swith")
while True:
    ch=int(input("enter the choice"))
    if ch ==1:
        print(var1+var2)
    elif ch ==2:
        print("Length of string",len(var1))
    elif ch==3:
        print("reverse",var1[::-1])
    elif ch==4:
        print("range",var2[2:5])
    elif ch==5:
        print("upper case",var1.upper())
    elif ch==6:
        print("lowercase",var2.lower())
    elif ch==7:
     for x in var1:{
          print(" ",x)
    }
    elif ch==8:
        print(var1*2)
    elif ch==9:
        print("splitting",var1.split())
    elif ch==10:
         print("numvber of c=occurenece",var1.count("T"))
         #  x = var1.startswith("T")
         # print(x)
    elif ch==11:
        print("T" in var1)
    else:
        quit