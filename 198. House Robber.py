class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = [0]*n
        if(n==0):
            return 0
        elif(n == 1):
            return nums[0]
        elif(n == 2):
            return max(nums[0],nums[1])
        
        ans[0] = nums[0]
        ans[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            ans[i] = max(nums[i]+ans[i-2],ans[i-1])
            
        return ans[-1]
