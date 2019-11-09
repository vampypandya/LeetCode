class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def find_sub(big, small):
            if(len(small) == 0):
                return True
            if(len(big)==0):
                return False
            search = small[0]
            for i,char in enumerate(big):
                if(char==search):
                    return find_sub(big[i+1:],small[1:])
                
            
        return find_sub(t,s)
        
