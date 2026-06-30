"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        timestamps = []

        for i in intervals:
            timestamps.append((i.start,1))
            timestamps.append((i.end,-1))

        timestamps.sort(key = lambda x:(x[0],x[1]))
        Meetingrooms = 0
        count = 0
        for t in timestamps:
            count+=t[1]
            Meetingrooms = max(Meetingrooms,count)
        
        return Meetingrooms


        