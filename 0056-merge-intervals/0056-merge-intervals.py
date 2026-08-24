class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()

        res=[]
        for i in intervals:
            start=i[0]
            end=i[1]
            if len(res)==0:
                res.append([i[0],i[1]])

            last=res[-1]
            if start<=last[1]:
                new_end=max(last[1],end)
                res[-1]=[last[0], new_end]
            else:
                res.append([start, end])
        return res

        
