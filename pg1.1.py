#10 operation on tuples
var1 =('a','b','c','d')
var2=(1,2,3,6,4,5)
thistuple = ("apple", "banana", "cherry")
print("1.conactenation")
print("2.length")
print("3slicing")
print("4.range slicing")
print("5.reprtation")
print("6.maximum")
print("7.min")
print("8.itration")
print("10.return true or false")
print("9.delete tuples")
while True:
    ch =int(input("enter your choice"))
    if ch==1:
        x=var1+var2
        print(x)
    elif ch==2:
        print(len(var1))
    elif ch==3:
        print("",var2[2])
    elif ch==4:
        print("range slicing",var2[2:4])
    elif ch==5:
        print(var1*2)
    elif ch==6:
        print(max(var2))
    elif ch==7:
        print(min(var2))
    elif ch==8:
        for x in var1:
            print(x)
    elif ch==9:
        del(var1)
        print(var1)
    elif ch==10:
         if "a" in var1:
             print("True")
    elif ch==11:
        thistuple = tuple(input("enter the value"))
        print(type(thistuple))
        print(thistuple)
    else:
        print("false")
        quit()