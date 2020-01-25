
d={}
d[0]=1 
d[1]=1


def fibonacci(n): #DP without Bottom up

    

    if n in d:
        return d[n]
    else:
        result= fibonacci(n-1)+fibonacci(n-2)
        d[n]=result
        return result
    

def fib(n): #recursive approach
    if n==1 or n==2:
        result=1
    else:
        result=fib(n-1)+fib(n-2)
    return result

def fibBottomUp(n):

    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]



print(fibBottomUp(100000))