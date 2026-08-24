class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroes=0
        ones=0
        freq={}
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
            else:
                ones+=1
            diff=zeroes-ones
            if diff==0:
                res=max(res, i+1)
            if diff not in freq:
                freq[diff]=i
            else:
                length=i-freq[diff]
                res=max(length, res)
        return res