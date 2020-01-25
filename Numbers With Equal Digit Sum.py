

def func(a):
    sum=0
    while a>0:
        sum=sum+int(a%10)
        a=int(a)/10
    return sum
d={}
nums=[51, 32, 43]
nums.sort()
for i in nums:
    if func(i) in d:

        d[func(i)].append(i)
    else:
        d[func(i)]=[]
        d[func(i)].append(i)

t=-float('inf')
z=-1
for i  in d:
    if len(d[i])>1:
            
        sums=sum(d[i][-2:])

        if sums>t:
            z=(d[i][-2],d[i][-1])
print (z)






