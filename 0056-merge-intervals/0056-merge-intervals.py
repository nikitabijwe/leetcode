class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort the intervals based on the start value of each interval
        intervals.sort(key=lambda x: x[0])

        merged = []  # Initialize an empty list to store the merged intervals
        
        # Iterate through each interval
        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval does not overlap with the previous one,
            # simply append the current interval to the list of merged intervals
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap, so merge the current and previous intervals by updating the end value
                # of the last interval in the merged list
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Return the list of merged intervals
        return merged