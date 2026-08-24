class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        rank={}
        for i in range(len(order)):
            char=order[i]
            rank[char]=i
        slist=list(s)
        slist.sort(key=lambda x: rank.get(x,26))
        return "".join(slist)