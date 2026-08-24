class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        nums.sort(key=lambda x:(freq[x], -x))
        return nums