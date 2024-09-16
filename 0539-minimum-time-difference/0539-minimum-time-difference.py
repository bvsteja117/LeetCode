class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        minutes_list = [timeToMinutes(time) for time in timePoints]
        minutes_list.sort()
        
        min_diff = float('inf')
        
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i-1])
        
        min_diff = min(min_diff, 1440 + minutes_list[0] - minutes_list[-1])
        
        return min_diff