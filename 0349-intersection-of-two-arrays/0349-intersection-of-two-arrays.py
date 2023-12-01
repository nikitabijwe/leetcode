# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         lst=[]
#         for i in range(len(nums1)):
#             if nums1[i] in nums2:
#                 lst.append(nums1[i])
#                 i+=1
#         return set(lst)

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of the two sets
        result_set = set1.intersection(set2)
        print(result_set, "result_set")

        # Convert the set to a list for the expected return type
        result_list = list(result_set)

        return result_list
