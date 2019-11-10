class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        
        ans = [[0 for x in range(len(colsum))]for x in range(2)]
        # chk_ans = [[0 for x in range(len(colsum))]for x in range(2)]
        # print ans,chk_ans
        alter = []
        for i,val in enumerate(colsum):
            # print i,val,upper,lower
            # print ans,val
            if(val == 0):
                ans[0][i] = 0
                ans[1][i] = 0
            elif(val == 2):
                ans[0][i] = 1
                ans[1][i] = 1
                upper = upper - 1
                lower = lower - 1
        
        for i,val in enumerate(colsum):
            if(val==0 or val == 2): 
                continue
            # alter.append(i)
            if(upper >0):
                ans[0][i] = 1
                ans[1][i] = 0
                upper = upper - 1
            else:
                ans[0][i] = 0
                ans[1][i] = 1
                lower = lower - 1
        
        if(upper == 0 and lower == 0):
            return ans
        else:
            return []
