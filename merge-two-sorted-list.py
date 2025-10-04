"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""







"""lets do it over"""

"""
LET ME EXPLAIN: 

list1 = [1,2,4] and list2 = [1,3,4]
mergedList = []

remember we have the pointer as current, which points to the next node in the merged list

so in both list 1 and 2 the very first node is 1, and 1 since they are equal, the else block is executed

so mergedList = [1]
list1 = [1,2,4]   list 2 = [3,4]

compare the very first val in each list again
since 1 is less than 3
1 will be moved to the merged list

mergedList = [1,1]  --> the current is the second 1

list 1 = [2,4]  list 2 = [3,4]

compare again, 2 is less than 3
so 2 moves to the mergedList[1,1,2]  current = 2

so we have list 1 = [4],  list 2 = [3,4]

compare again 3 is less than  4 so 3 moves to the sorted mergedList
mergedList = [1,1,2,3]


and on and on it goes



Now lets implement the code

mind the indentations
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeList(list1:ListNode, list2: ListNode)-> ListNode:
    head = ListNode()
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    """Step 4: Handle any remaining nodes
    # If list1 has remaining nodes, append them"""
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return head.next

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print a linked list
def printLinkedList(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)



list1 = createLinkedList([1, 2, 4])  # Convert the array to a linked list
list2 = createLinkedList([1, 3, 4])  # Convert the array to a linked list

# Merge the two linked lists
merged_list = mergeList(list1, list2)

# Print the merged linked list
printLinkedList(merged_list)










