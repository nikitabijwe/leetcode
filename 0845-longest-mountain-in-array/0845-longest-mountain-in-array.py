class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_length = 0
        
        for i in range(1, n - 1):  # Start from the second element and end before the last element
            if arr[i - 1] < arr[i] > arr[i + 1]:  # Check if the element is a peak of a mountain
                left = right = i  # Initialize left and right pointers
                # Expand left to find the increasing part of the mountain
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                # Expand right to find the decreasing part of the mountain
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                # Update the maximum length of the mountain found so far
                max_length = max(max_length, right - left + 1)
        
        return max_length if max_length >= 3 else 0  # Return the maximum length of the mountain