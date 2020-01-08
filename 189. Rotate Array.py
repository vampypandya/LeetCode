class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        m = len(nums)
        first = nums[m - k:]
        second = nums[0:m - k]
        first.extend(second)
        for i in range(len(nums)):
            nums[i] = first[i]

