"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if
 every element is distinct.



Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.


EXPLANATION


Let's Trace Your Array [1, 2, 3, 1]
python
numbers = [1, 2, 3, 1]
seen = {}  # Empty dictionary

# First number: 1
if 1 in seen:  # Is 1 in the dictionary? NO
seen[1] = 1    # ADD 1 to dictionary → seen = {1: 1}

# Second number: 2
if 2 in seen:  # Is 2 in the dictionary? NO
seen[2] = 1    # ADD 2 to dictionary → seen = {1: 1, 2: 1}

# Third number: 3
if 3 in seen:  # Is 3 in the dictionary? NO
seen[3] = 1    # ADD 3 to dictionary → seen = {1: 1, 2: 1, 3: 1}

# Fourth number: 1
if 1 in seen:  # Is 1 in the dictionary? YES! ← DUPLICATE FOUND!
return True
The Value = 1 is Just a Placeholder
The value doesn't matter - we only care about the keys in the dictionary:
"""

# def contains_duplicates(nums:list):
#     if len(nums) < 2:
#         return nums
#     nums.sort()
#     i = 0
#     duplicates = 0
#     while i < len(nums) - 1:
#         if nums[i] == nums[i+1]:
#             duplicates+=2
#             i+=2
#         else:
#             i+=1
#     return f"The amount of duplicates is {duplicates}"
# print(contains_duplicates([1,2,3,4,1]))


"""better solution with o(1) time"""

def contains_duplicates(nums):
    if len(nums) < 2:
        return False
    count = dict()

    for num in nums:
        if num in count:
            return True
        count[num] = 1
    return False
print(contains_duplicates([1,2,3,4,1]))

