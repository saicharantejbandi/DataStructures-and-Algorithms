nums=[]
def searchInsert(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums)
    while(l<r):
        m = (l+r)//2
        if nums[m] > target:
            r = m
        elif nums[m] < target:
            l = m+1
        else:
            print(m)
    print(l)