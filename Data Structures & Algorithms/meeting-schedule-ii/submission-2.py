"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        count =1
        s = 1
        Max = 1
        e = 0
        
        while s<len(intervals):
            if start[s]<end[e]:
                s+=1
                count+=1
                Max = max(count,Max)
            else:
                e+=1
                count-=1
                Max = max(count, Max)
        return Max