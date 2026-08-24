class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        for x in nums:
            sum+=x
        left=0
        right=0
        for i in range(len(nums)):
            right=sum-left-nums[i]
            if left==right:
                return i
            left=left+nums[i]
        return -1

           