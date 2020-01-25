def binarySearch(lis, start, end, target):
    

    mid=int((start+end)/2)
    #print (mid)

    if mid==start or mid==end:
        if target== lis[mid]:
            return mid
        else:
            return -1

    elif target==lis[mid]:
        return mid
    elif target <lis[mid]:
       return binarySearch(lis,start,mid-1,target)
    else:
        return binarySearch(lis,mid+1,end,target)



print(binarySearch([1,2,3,4,5,6,7], 0,6,100))