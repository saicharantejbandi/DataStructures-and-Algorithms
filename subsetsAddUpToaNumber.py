def count_sets(arr,total):
   
  
    return recDp(arr,total,len(arr)-1)

d={}

def recDp(arr,total,m):

    key=str(total)+str(":")+str(m)
    if key in d:
        return d[key]


    if total==0:
        return 1
    elif total<0:
        return 0
    elif m<0:
        return 0
    elif total<arr[m]  :
        k=rec(arr,total,m-1)
        #return rec(arr,total,m-1)
    else:

        k= rec(arr,total-arr[m],m-1)+rec(arr,total,m-1)
    d[key]=k
    return k
















def rec(arr,total,m):
    if total==0:
        return 1
    elif total<0:
        return 0
    elif m<0:
        return 0
    elif total<arr[m]:

        return rec(arr,total,m-1)
    else:
        return rec(arr,total-arr[m],m-1)+rec(arr,total,m-1)



arr=range(0,150)
print(count_sets(arr,100))

