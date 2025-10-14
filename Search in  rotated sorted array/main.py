"""


33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown
ndex k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2] , target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


    Explanation


The Core Logic:

Check which half is sorted using nums[left] <= nums[mid]

If left half is sorted:

If target is within [nums[left], nums[mid]), search left

Else search right

If right half is sorted:

If target is within (nums[mid], nums[right]], search right

Else search left

Why This Works:

In a rotated array, one half is always properly sorted

We can efficiently eliminate half the search space each iteration

The distinct values guarantee no duplicates to complicate comparisons

"""
# def search(nums:list, target:int):
#     if not nums:
#         return 'Error'
#     left, right = 0, len(nums) -1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         if nums[left] <= nums[mid]:
#             if nums[left] <= target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         else:
#             if nums[mid] < target <= nums[right]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return -1
# print(search([4,5,6,7,0,1,2], 2))















def search(nums:list, target:int):
    if not nums:
        return 'Error'
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        """check if left half is sorted"""
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search([4,5,6,7,0,1,2], 0))