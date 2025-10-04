"""
given an array of integer nums and integer target, return the indexes of two numbers such that
they add up to the target, rg, [2,4,5,6,7] target is 7

solve:
"""

# def array(array_list):
#     target = array_list[4]
#     res = []
#     for i in range(array_list):
#         if array_list[i] + array_list[i] == target:
#             return True
#     return None
# array([2,4,5,6,7])


# numbers_dict = {
#     "int": [2,4,5,6,7]
# }
#
# for value in numbers_dict.values():
#     target = 7
#     if value + value == target:
#         print("TRue")
#     else:
#         print("false")


# def find_indexes(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return None
# print(find_indexes([2,4,5,6,7], 7))

# nums = [1,2,3,4,5]  [2,3,4,5] [3,4,5]  [4,5]

# for i in range(len(nums)):
#     print(i)
#     for j in range(i+1, len(nums)):
#         print(j)


# def find_indexes(nums:list, target:int):
#     for i in range(len(nums)):
#         for j in range(1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#     return None
# print(find_indexes([2,4,5,6,7], 7))

"""we run the first for loop - outer which is 0-4
we run the second for loop  - inner adn compare it with the outer
it will be like 1-4, 2-4, 3-4, since its i + 1 so it starts from the next number"""

def two_sum(nums:list, target:int):
    if not nums:
        return f"nums is empty"
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
fd = two_sum([1,2,4,5], 6)
print(fd)






















"""REVISITING THE TWO SUMS ALGO"""
# def two_sum_algo(array:list, target:int):
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             if array[i] + array[j] == target:
#                 return [i, j]
#     return None
#
# print(two_sum_algo([1,2,3,4,5,6,9], 9))



# array = [1,2,3,4,5]
#
# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         print(j)