class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        ans = [[0 for x in range(m)] for y in range(n)]
        r_sum = [1]*n
        c_sum = [1]*m
        cnt = 0
        for pair in indices:
            r,c = pair[0],pair[1]
            ans[r] = [x+1 for x in ans[r]]
            for ele in ans[r]:
                if(ele%2 != 0):
                    cnt = cnt + 1
                else:
                    cnt= cnt - 1
            for i in range(n):
                ans[i][c] = ans[i][c]+1
                if(ans[i][c] % 2!=0):
                    cnt = cnt + 1
                else:
                    cnt = cnt - 1

        
        return cnt
        
