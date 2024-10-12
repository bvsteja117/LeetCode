class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        q = []
        for left, right in sorted(intervals):
            if q and q[0] < left:
                heappop(q)
            heappush(q, right)
        return len(q)

        