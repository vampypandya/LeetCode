class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start = 0
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        for arr in matrix[::-1]:
            if (arr[0] <= target):
                for i, ele in enumerate(arr[start:]):
                    if (ele == target):
                        return True
                    elif (ele > target):
                        start = i
                        break
        return False


