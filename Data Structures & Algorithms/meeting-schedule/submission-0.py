"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        self.sorted_intervals = []

        def add_interval(sorted_list_index: int, interval_to_add: Interval) -> bool:

            # if first entry to be added
            if sorted_list_index < 0:
                self.sorted_intervals.append(interval_to_add)
                return True
            else:
                interval_to_match = self.sorted_intervals[sorted_list_index]

                # check if incoming meeting is after the last meeting
                if interval_to_add.start >= interval_to_match.end:
                    self.sorted_intervals.insert(sorted_list_index+1, interval_to_add)
                    return True
                
                # check if incoming meeting is between the last meeting
                elif interval_to_add.start >= interval_to_match.start or interval_to_add.end > interval_to_match.start:
                    return False

                # meeting is before the last meeting
                else:

                    # if there are no further meetings to match
                    if sorted_list_index == 0:
                        self.sorted_intervals.insert(0, interval_to_add)
                        return True

                    # check with next meeting
                    else:
                        return add_interval(sorted_list_index-1, interval_to_add)

        for interval in intervals:
            possible_to_add = add_interval(len(self.sorted_intervals)-1, interval)
            if not possible_to_add:
                return False

        return True
            
