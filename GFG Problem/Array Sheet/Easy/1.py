# 1.Merge Intervals
# Problem:Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
def merge_intervals(intervals):
    intervals.sort()
    
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]