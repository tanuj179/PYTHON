from multipledispatch import dispatch
@dispatch(bool)
def hello(a):
    print("hello there")
@dispatch(str)
def hello(a):
    print(f"hello from {a} ")
@dispatch(str,int)
def hello(s,b):
    print(f"hello from {s} and his age is {b}")
@dispatch(int,int)
def sum(a,b):
    print(f"THE SUM IS {a+b}")
@dispatch(int,int,int)
def sum(a,b,c):
    print(f"THE SUM IS {a+b+c}")
@dispatch(int,float,float)
def sum(a,b,c):
    print(f"The sum is {a+b+c}")
print("1.hello method with no parameter")
print("2. hello method with one parameter")
print("3. hello method with 2 parameter")
print("4. sum method with 2 parameter")
print("5.sum method with 3 parameter")
print("6.sum method with 3 paramaeter")
while True:
    ch =int(input("enter the choicee"))
    if ch==1:
        hello(True)
    elif ch==2:
        a=input("enter the name ")
        hello(a)
    elif ch==3:
        s=input("enter the name : ")
        b=int(input("enter the age : "))
        hello(s,b)
    elif ch==4:
        a=int(input("enter the first value : "))
        b=int(input("enter the second value : "))
        sum(a,b)
    elif ch==5:
        a=int(input("enter the first value : "))
        b=int(input("enter the second value : "))
        c=int(input("enter the third value : "))
        sum(a,b,c)
    elif ch==6:
        a=int(input("enter the first value ineteger : "))
        b=float(input("enter the second value  float : "))
        c=float(input("enter the third value float : "))
        sum(a,b,c)
    else:
        quit()
        