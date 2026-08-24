class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        cur_sum=0
        prefix={0:1}
        for i in range(len(nums)):
            cur_sum+=nums[i]
            target=cur_sum-k
            if target in prefix:
                count+=prefix[target]
            prefix[cur_sum]=prefix.get(cur_sum, 0)+1
        return count