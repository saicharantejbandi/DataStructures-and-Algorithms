# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return None
            
        
        re=[]
        
        q=[]
        q.append(root)
        
        while len(q)!=0:
            
            p=len(q)
            z=[]
            
            for i in range(p):
                k=((q.pop(0)))
                z.append(k.val)
                
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
                    
                    
            re.append(max(z))
        print(re)
                
            
        
        
        
        