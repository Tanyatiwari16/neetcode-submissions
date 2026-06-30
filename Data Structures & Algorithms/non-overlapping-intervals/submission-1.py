class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda pair: pair[0])
        prev = intervals[0][1]

        res = 0

        for start, end in intervals[1:]:

            if prev>start:

                res+=1
                prev = min(prev,end)
            else:
                prev = end

        return res
        