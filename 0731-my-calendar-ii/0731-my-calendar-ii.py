class MyCalendarTwo(object):

    def __init__(self):
    
        self.booked = list()
       
        self.overlaped = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for os, oe in self.overlaped:
            if max(os, start) < min(oe, end):
                return False
        for bs, be in self.booked:
            ss = max(bs, start)
            ee = min(be, end)
            if ss < ee:
                self.overlaped.append((ss, ee))
        self.booked.append((start, end))
        return True