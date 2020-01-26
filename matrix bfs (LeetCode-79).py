class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
    
        #d=[]
        length=len(board[0])
        height=len(board)
        wordl=len(word)
       
        #d=[]
        def search(i,k,count,s):
            
        
            if count==wordl:
                return True
            
            
            if i<0 or i>=height or k<0 or k>= length or board[i][k]!=word[count] or count>wordl or [i,k] in d :
                return False
            
            #t=board[i][k]
            #board[i][k]=" "
            d.append([i,k])
            s=s+board[i][k]
            if search(i+1,k,count+1,s) or search(i-1,k,count+1,s) or search(i,k+1,count+1,s) or search(i,k-1,count+1,s) :
                return True
            else:
                d.remove([i,k])
                #board[i][k]=t
                return False
           
            
        for i in range(height):
            for k in range(length):
                if board[i][k]==word[0]:
                    d=[]
                    s=""
                    count=0
                    if  search(i,k,count,s):
                        return True
        
        return False