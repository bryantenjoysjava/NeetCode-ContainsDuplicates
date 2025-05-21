"""Given an integer array nums1 and nums 2,
return True if any value appears
 more than once in the array, otherwise
 return false"""
class Solution:
     @staticmethod
     def hasDuplicate(nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


nums1 = [1,2,3,4]
nums2 = [1,2,2,4]
print(Solution.hasDuplicate(nums1))
print(Solution.hasDuplicate(nums2))