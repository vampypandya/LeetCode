class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_c = []
        s_t = []
        for ele in S:
            if(ele=='#'):
                if(len(s_c)>0):
                    s_c.pop()
            else:
                s_c.append(ele)
        
        for ele in T:
            if(ele=='#'):
                if(len(s_t)>0):
                    s_t.pop()
            else:
                s_t.append(ele)
        if(s_t>=0 and s_c>=0 and s_t == s_c):
            return True
        else:
            return False
            
