class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high=-1
        count=0
        for i in nums:
            if i>=high:
                high=i
                count+=1
            else:
                continue
        return count