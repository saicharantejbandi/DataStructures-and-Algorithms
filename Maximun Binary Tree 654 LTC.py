# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        re=TreeNode(max(nums))
        temp=re
        
        
        def build2(temp,tempr,templ):
            temp.left=templ
            temp.right=tempr
            return temp        
        
        def build(arr):
            
            
            if len(arr)>0:
                
                maxi=arr.index(max(arr))
                temp=TreeNode(arr[maxi])
                aright=arr[maxi+1:]
                aleft=arr[:maxi]
                temp.right=build(aright)
                temp.left=build(aleft)
                return temp
            
                
            
            
            
        
        return (build(nums))
            

            
            
            