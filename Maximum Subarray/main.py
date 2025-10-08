"""

53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""


# def maximum_subarray(nums:list):
#     if len(nums) < 3:
#         return f"{nums} does not meet the criteria for execution"
#     maxSum = nums[0]
#
#     for i in range(len(nums)):
#         curSum = 0
#         for j in range(i+1, len(nums)):
#             curSum += nums[j]
#             maxSum = max(maxSum, curSum)
#     return maxSum

# print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))



"""Optimized Approach

in this approach, we are going to overlook it, anytime we come across a negative number

so in the list provided be adding them numbers together, once you arrive at a negative number, know that it will be
discarded, only add and store positive nums

kadane's algorithm

"""

def maxSubArray(nums:list):
    if not nums:
        return 'Error'
    maxSum = nums[1]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# def maximumSubarray(nums:list):
#     if len(nums) < 3:
#         return f"{nums} did not meet the requirement"
#     maxSum = nums[0]
#     curSum = 0
#
#     for n in nums:
#         curSum = max(curSum, 0)
#         curSum += n
#         maxSum = max(maxSum, curSum)
#     return maxSum
#
# res = maximumSubarray([-2,1,-3,4,-1,2,1,-5,4])
# print(res)