"""

238. Product of Array Except Self
Medium
Topics
premium lock icon
Companies
Hint

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Let me explain, answer[i] is equal to the product of all elements of nums except nums[i]

sp at the beginning nums[i] is 1 => so we multiply the rest of the numbers except 1, that will give us 24
next we go to nums[i] = 2 so we multiply the numbers except 2 , 1x3x4 = 12 and so on
"""



"""Brute force approach"""

def productOfArrayExceptSelf(nums:list):
    if len(nums) < 3:
        return 'Does not meet the standard'
    n = len(nums)
    result_array = [1] * n

    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result_array[i] = product
    return result_array
print(productOfArrayExceptSelf([1,2,3,4]))


# def productExceptSelf_bruteForce(nums):
#     n = len(nums)
#     answer = [1] * n  # Initialize with 1's
#
#     for i in range(n):
#         product = 1
#         # Multiply all elements except the one at position i
#         for j in range(n):
#             if i != j:  # Skip the current element
#                 product *= nums[j]
#         answer[i] = product
#
#     return answer
#
#
# # Test
# print(productExceptSelf_bruteForce([1, 2, 3, 4]))  # [24, 12, 8, 6]

"""trying to explain

i equals
j equlas
i        j
0         0
1         1
2          2
3          3


so we are actually comapring values    
[1,2,3,4]  = i
[1,2,3,4] = j

so we first loop through i, then in the inner loop, we loop through j


in the inner loop, 

product = 1  # Reset product to 1 for this position


note we are comparing j with i!!
j = 0: if 0 != 0? NO → skip (don't multiply nums[0])
j = 1: if 0 != 1? YES → product *= nums[1] → 1 × 2 = 2
j = 2: if 0 != 2? YES → product *= nums[2] → 2 × 3 = 6  
j = 3: if 0 != 3? YES → product *= nums[3] → 6 × 4 = 24

Array: [1, 2, 3, 4]
         ↑   ↑  ↑  ↑
Index:   0   1  2  3

We're at i = 0 (value = 1)
We want: product of ALL elements EXCEPT the one at i=0

So we check each j:
j=0: i=0, j=0 → i == j → SKIP nums[0] (the 1)
j=1: i=0, j=1 → i != j → MULTIPLY nums[1] (the 2)  
j=2: i=0, j=2 → i != j → MULTIPLY nums[2] (the 3)
j=3: i=0, j=3 → i != j → MULTIPLY nums[3] (the 4)

Result: 2 × 3 × 4 = 24

the same goes for the rest


"""


# def product_of_array(nums:list):
#     """base case"""
#     if len(nums) < 3:
#         return f"cannot execute, this is nums: {nums}"
#     n = len(nums)
#     answer_list = [1] * n
#
#     for i in range(n):
#         product = 1
#         for j in range(n):
#             if i != j:
#                 product *= nums[j]
#         answer_list[i] = product
#     return answer_list
#
# print(product_of_array([1,2,3,4,5,6,7,8,9]))


