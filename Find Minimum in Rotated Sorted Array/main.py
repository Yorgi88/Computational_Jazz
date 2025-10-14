"""

153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

This problem uses binary search, but not in the traditional way. We're searching for the
inflection point where the array "breaks" from ascending order.

The array has two sorted portions, lets call them left and right

[3,4,5,1,2] , left will [3,4,5] , right will be [1,2]

inflection point, between 5 and 1


"""
def findMin(nums:list):
    if not nums:
        return 'Error'
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    return f"Answer is {nums[left]}"
print(findMin([3,4,5,1,2]))

















# def findMinimum(nums:list):
#     if not len(nums):
#         return 'Error'
#     left, right = 0, len(nums)-1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] > nums[left]:
#             left = mid + 1
#         else:
#             right = mid
#     return nums[left]
#
# print(findMinimum([3,4,5,1,2]))











# def findMin(nums:list):
#     if not nums:
#         return False
#     left, right = 0, len(nums) - 1
#
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] > nums[right]:
#             left = mid + 1
#         else:
#             right = mid  #since its possible that the mid can also be the smallest
#     return nums[left]
# print(findMin([3,4,5,1,2]))