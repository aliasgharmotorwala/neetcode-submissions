class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        l = 0
        r = len(intervals)-1

        if r < 0:
            return [newInterval]
        elif r < 1:
            m = 0

        # Binary search to get the closest interval to the new interval
        while l <= r:

            m = (l+r)//2 # 0

            #  end of new interval < start of middle interval >> go left
            if newInterval[1] < intervals[m][0]:
                r = m - 1
            # start of new interval > end of middle interval >> go right
            elif newInterval[0] > intervals[m][1]: # 2 < 
                l = m + 1
            else:
                break

        output = []
        
        # if the new interval is before the middle interval
        if newInterval[1] < intervals[m][0]:
            output = intervals[:m]
            output.append(newInterval)
            output = output + intervals[m:]

        # if the new interval is after the middle interval
        elif newInterval[0] > intervals[m][1]:
            output = intervals[:m+1]
            output.append(newInterval)
            output = output + intervals[m+1:]

        else:

            # if there is a overalap, merge both intervals
            new_interval = [min(newInterval[0], intervals[m][0]), max(newInterval[1], intervals[m][1])]
        
        
            # check if the left side interval is not overlaping, merge if yes
            i = m-1
            while i >= 0:
                if new_interval[0] <= intervals[i][1]:
                    new_interval[0] = min(new_interval[0], intervals[i][0])
                    i -= 1
                else:
                    break

            # check if the right side interval is not overlaping, merge if yes
            j = m+1
            while j < len(intervals):
                if new_interval[1] >= intervals[j][0]:
                    new_interval[1] = max(new_interval[1], intervals[j][1])
                    j += 1
                else:
                    break
        
            output = intervals[:i+1]
            output.append(new_interval)
            output = output + intervals[j:]

        return output