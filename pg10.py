from re import A, T
from time import time
from wsgiref.validate import WriteWrapper
def Calc_time(fn):
    def wrapper(*args,**kwargs):
        t1=time()
        result=fn(*args,**kwargs)
        t2=time()
        t=(t2-t1)*1000
        print("THe time Differnce to pass ann object in function in seconds : ",t)
        return result
    return wrapper
@Calc_time
def fib(num):
    a=0
    b=1
    for i in range(0,num):
        yield a
        a,b=b,a+b
n=int(input("enter the value of n : "))
for x in fib(n):
    print(x)
        