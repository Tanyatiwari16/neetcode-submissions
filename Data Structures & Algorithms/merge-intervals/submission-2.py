class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key =  lambda x: x[0])
        newint = [intervals[0]]

        for start, end in intervals:

            if newint[-1][1]< start:
                newint.append([start,end])
            else:

                newint[-1][1] = max(newint[-1][1] ,end)

        return newint

