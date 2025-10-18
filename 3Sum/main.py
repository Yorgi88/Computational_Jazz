"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.


Explanation

Read Carefully
------------------------
Sort the number first

Step 2: Fix First Number and Find Partners
Fix -4: Need two numbers that add up to 4

Look at numbers after -4: [-1, -1, 0, 1, 2]

Start with left=-1 and right=2: -1 + 2 = 1 (too small)

Move left to next -1: -1 + 2 = 1 (too small)

Move left to 0: 0 + 2 = 2 (too small)

Move left to 1: 1 + 2 = 3 (too small)

No solution with -4

---->

Fix -1: Need two numbers that add up to 1

Look at numbers after -1: [-1, 0, 1, 2]

Start with left=-1 and right=2: -1 + 2 = 1 ✓ FOUND!

Triplet: [-1, -1, 2]

Fix next -1: Skip because it's the same as previous

Fix 0: Need two numbers that add up to 0

Look at numbers after 0: [1, 2]

1 + 2 = 3 (too big)

No solution




----------------------


code explanation

---------------------------


1. Understanding the Setup
python
nums.sort()  # Step 1: Sort the numbers
result = []
What this does:

nums.sort() rearranges the array in ascending order

[-1,0,1,2,-1,-4] becomes [-4,-1,-1,0,1,2]

result = [] creates an empty list to store our answers

Why sort? Sorting helps us:

Find numbers efficiently using two pointers

Skip duplicates easily

Avoid getting the same answer multiple times

2. The Main Loop - Fixing Each Number
python
for i in range(len(nums)):
What this does:

Goes through each position in the array

i will be our first number in the triplet

For 6 numbers: i = 0,1,2,3,4,5

3. Skipping Duplicates
python
if i > 0 and nums[i] == nums[i-1]:
    continue
What this means:

i > 0 means "if we're not at the first element"

nums[i] == nums[i-1] means "if current number equals previous number"

continue means "skip this iteration and go to the next one"

Example:

text
Array: [-4, -1, -1, 0, 1, 2]
When i=2: nums[2] = -1, nums[1] = -1 → they're equal → SKIP!
This prevents getting [-1,-1,2] twice
4. Setting Up the Two Pointers
python
target = -nums[i]
left = i + 1
right = len(nums) - 1
What this does:

target = -nums[i]: If our first number is a, we need b + c = -a

left = i + 1: Start searching from the next element

right = len(nums) - 1: Start from the last element

Example with i=1 (nums[i] = -1):

text
target = -(-1) = 1
left = 2 (points to -1)
right = 5 (points to 2)
We're looking for two numbers between indices 2-5 that add up to 1
5. The Two Pointer Search
python
while left < right:
What this means:

Keep searching as long as left hasn't passed right

When left >= right, we've checked all possible pairs

6. Checking the Current Sum
python
current_sum = nums[left] + nums[right]
What this does:

Adds the numbers at left and right positions

We compare this sum with our target

7. Case 1: Found a Match!
python
if current_sum == target:
    result.append([nums[i], nums[left], nums[right]])
What happens:

We found three numbers that sum to zero!

Add the triplet to our result list

Example: [-1, -1, 2] gets added to result

8. Skipping Duplicates After Finding a Match
python
# Skip any duplicates on left side
while left < right and nums[left] == nums[left + 1]:
    left += 1
# Skip any duplicates on right side
while left < right and nums[right] == nums[right - 1]:
    right -= 1
What this does:

First while loop: If the next number is the same, move left forward

Second while loop: If the previous number is the same, move right backward

Example:

text
If we have [... -1, -1, -1, 0, 1 ...] and left points to first -1
The loop moves left past all the -1's to point to 0
9. Moving Both Pointers
python
left += 1
right -= 1
What this does:

After finding a match, move both pointers inward

We've used the current left and right numbers, so try new ones

10. Case 2: Sum is Too Small
python
elif current_sum < target:
    left += 1
What this means:

nums[left] + nums[right] is less than what we need

Since array is sorted, moving left right gives us a bigger number

11. Case 3: Sum is Too Large
python
else:
    right -= 1
What this means:

nums[left] + nums[right] is more than what we need

Since array is sorted, moving right left gives us a smaller number

Complete Walkthrough with [-4,-1,-1,0,1,2]
Iteration 1: i=0 (fix -4)

Target = 4

left=1 (-1), right=5 (2): -1+2=1 < 4 → left=2 (-1)

-1+2=1 < 4 → left=3 (0)

0+2=2 < 4 → left=4 (1)

1+2=3 < 4 → left=5 → stop (left >= right)

Iteration 2: i=1 (fix -1)

Target = 1

left=2 (-1), right=5 (2): -1+2=1 == 1 ✓

Add [-1,-1,2] to result

Skip duplicates, move pointers: left=3, right=4

left=3 (0), right=4 (1): 0+1=1 == 1 ✓

Add [-1,0,1] to result

Move pointers: left=4, right=3 → stop (left >= right)

Iteration 3: i=2 (fix -1)

Skip because same as previous

Iteration 4: i=3 (fix 0)

Target = 0

left=4 (1), right=5 (2): 1+2=3 > 0 → right=4

left=4 (1), right=4 (1): 1+1=2 > 0 → stop

Final result: [[-1,-1,2], [-1,0,1]]

This method efficiently finds all unique triplets without checking every possible combination!

"""

def threeSum(nums:list)->list or str or bool:
    if not nums or len(nums) < 3:
        return f"Error in {nums}"

    """we make our lives easier by sorting the nums"""
    nums.sort()
    result = []

    for i in range(len(nums)):
        """we check if the nums contains duplicates, if it does, move on to the next num"""
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == target:
                result.append([nums[i], nums[left], nums[right]])
                """if we encounter dups"""
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                right -= 1
    return result

print(threeSum([-1,0,1,2,-1,-4]))












# def threeSum(nums:list):
#     if not nums or len(nums) < 3:
#         return 'Error'
#
#     nums.sort()
#     res = list()
#
#     """initialize the for loop here"""
#     for i in range(len(nums)):
#         """we need to check for duplicates first"""
#         if i > 0 and nums[i] == nums[i-1]:
#             continue
#
#         """we define the variables here"""
#         target = -nums[i]
#         left = i + 1
#         right = len(nums) - 1
#
#         while left < right:
#             currentSum = nums[left] + nums[right]
#
#             if currentSum == target:
#                 res.append([nums[i], nums[left], nums[right]])
#                 """
#                 here we need to find out if there are other matches, apart from the
#                 res, so we need to check if there are actually duplicates, if there are, skip to the next
#                 if its from the right side, go backwards
#                 """
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 """here we push the pointer forward"""
#                 left += 1
#                 right -= 1
#             elif currentSum < target:
#                 left += 1
#             else:
#                 right -= 1
#     return res
#
# print(threeSum([-1,0,1,2,-1,-4]))
