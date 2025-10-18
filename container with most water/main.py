"""

11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1



Key Points to Understand:
You pick ANY two lines to form a container

The container cannot be slanted - the water level is determined by the shorter line

The width is the distance between the two lines

The height is the minimum of the two line heights

Goal: Find the pair that gives the maximum area


"""

def maxArea(height):
    if not height:
        return 'invalid'
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        distance = right - left
        container_height = min(height[left], height[right])

        area = container_height * distance
        max_area = max(max_area, area)

        """move the left pointer forward"""
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
print(maxArea([1,8,6,2,5,4,8,3,7]))