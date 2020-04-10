



def quickSort(arr):

    if len(arr)<=1:
        return arr
    
    else:
        mid=int((len(arr)-1)/2)
        a=[]
        b=[]
        c=[]
        for i  in arr:
            if i<arr[mid]:
                a.append(i)
            elif i>arr[mid]:
                b.append(i)
            else:
                c.append(i)        
        x=quickSort(a)
        y=quickSort(b)
        
        return x+c+y

print(quickSort([7,6,5,4,3,2,1,1]))

        
