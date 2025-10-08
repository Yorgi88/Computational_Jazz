"""
152. Maximum Product Subarray
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


explanation

if not nums:
    return 0

# Initialize with first element
max_so_far = nums[0]  # = 2
min_so_far = nums[0]  # = 2
result = nums[0]      # = 2
What we have after initialization:

max_so_far = 2 (max product ending at position 0)

min_so_far = 2 (min product ending at position 0)

result = 2 (global maximum so far)


-----

Iteration 1: i = 1, current = 3
python
current = nums[1]  # = 3

# Store temporary max because we'll overwrite it
temp_max = max(current, max_so_far * current, min_so_far * current)
Calculate the three candidates for temp_max:

current = 3

max_so_far * current = 2 × 3 = 6

min_so_far * current = 2 × 3 = 6

temp_max = max(3, 6, 6) = 6

min_so_far = min(current, max_so_far * current, min_so_far * current)

Calculate the three candidates for min_so_far:

current = 3

max_so_far * current = 2 × 3 = 6

min_so_far * current = 2 × 3 = 6

min_so_far = min(3, 6, 6) = 3

python
max_so_far = temp_max  # max_so_far = 6
result = max(result, max_so_far)  # result = max(2, 6) = 6
After Iteration 1:

max_so_far = 6 (from subarray [2,3])

min_so_far = 3

result = 6
-----


Iteration 2: i = 2, current = -2
python
current = nums[2]  # = -2

temp_max = max(current, max_so_far * current, min_so_far * current)
Calculate the three candidates for temp_max:

current = -2

max_so_far * current = 6 × -2 = -12

min_so_far * current = 3 × -2 = -6

temp_max = max(-2, -12, -6) = -2

python
min_so_far = min(current, max_so_far * current, min_so_far * current)
Calculate the three candidates for min_so_far:

current = -2

max_so_far * current = 6 × -2 = -12

min_so_far * current = 3 × -2 = -6

min_so_far = min(-2, -12, -6) = -12

python
max_so_far = temp_max  # max_so_far = -2
result = max(result, max_so_far)  # result = max(6, -2) = 6
After Iteration 2:

max_so_far = -2 (from subarray [-2])

min_so_far = -12 (from subarray [6,-2] or [3,-2])

result = 6



------> and so on till you reach when i = 3 and that the number 4




"""

def maximum_product_subarray(nums:list):
    if not nums:
        return 'Error'
    maxForNow = nums[0]
    minForNow = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if i == 0:
            return 0
        current = nums[i]

        tmp_max = max(current, current*maxForNow, current*minForNow)
        minForNow = min(current, current*maxForNow, current*minForNow)
        maxForNow = tmp_max
        result = max(result, maxForNow)
    return result
print(maximum_product_subarray([2,3,-2,4]))