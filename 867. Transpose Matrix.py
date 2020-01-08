class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(A), len(A[0])
        ret = [[0] * m for _ in range(n)]
        print
        ret

        for i in range(n):
            for j in range(m):
                ret[i][j] = A[j][i]

        return ret

