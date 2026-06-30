"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if len(intervals)<=1:
            return True
        temp = intervals[0]
        for i in intervals[1:]:
            if i.start<temp.end:
                return False
            else:
                temp = i
        return True