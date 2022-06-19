a=[1,4,9,3,5,6,7]
b=[2,4,6,7]
print("1.length of list")
print("2.cocatenation")
print("3.repetation")
print("4.slicing")
print("5.range slicing")
print("6 maximum")
print("7.minimum")
print("8.iteration")
print("9.inseting an element")
print("10 TRue or false")
while True:
    ch =int(input("enter the choice"))
    if ch==1:
        print(len(a))
    elif ch==2:
        c=a+b
        print(c)
    elif ch==3:
        print(a*3)
    elif ch==4:
        print(a[5])
    elif ch==5:
        print(a[2:5])
    elif ch==6:
        print(max(b))
    elif ch==7:
        print(min(a))
    elif ch==8:
        for x in a:
            print(x)
    elif ch==9:
        print(a.insert(10,101))
        print(a)
    elif ch==10:
        a.sort()
        print(a)
    else:
        quit()