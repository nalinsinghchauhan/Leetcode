class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        cur_sum=0
        rem={0:1}
        for i in nums:
            cur_sum+=i
            remainder=cur_sum%k
            if remainder in rem:
                count+=rem[remainder]
            rem[remainder]=rem.get(remainder, 0)+1
        return count
        