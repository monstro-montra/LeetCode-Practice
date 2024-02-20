'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def addTwoNumbers(linkedList1, linkedList2):
        dummyHead = ListNode(0) # placeholder
        current = dummyHead # starts pointing to dummyHead, but will be used to append to result list and iterate through both lists.
        carry = 0 # used to store any carry-over from the sum of two digits that exceed 9. updated in each iteration of the loop

        while linkedList1 or linkedList2 or carry: # loop until all digits from both linked lists and carry are processed.
            # extract current value of linkedLists. Otherwise, it's 0. This is to add padding to shorter lists with 0's.
            val2 = linkedList2.val if linkedList2 else 0 
            val1 = linkedList1.val if linkedList1 else 0 

            # calculate the sum of the current digits from both lists and any carry 
            sum = val1 + val2 + carry 

            # integer division of sum by 10. if sum is 10 or more, carry will be 1 indicating a carry and 0 will be no carry.
            carry = sum // 10
            current.next = ListNode(sum % 10) # create new list node with the digit, sum % 10. represents current digit of sum to add to results.
            current = current.next # update the current pointer to the new node just added.

            # check if there are more digits to process in eached linked list. if there are, advance the pointers into the next node in their lists.
            if linkedList1:
                linkedList1 = linkedList1.next
            
            if linkedList2:
                linkedList2 = linkedList2.next

        # after loop, return the sum as a linkedlist. it points to the head of the result list, excluding the dummy node.
        return dummyHead.next

# Helper function to create a linked list from a list of values
def createLinkedList(elements):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in elements:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

# Example usage
l1 = createLinkedList([2, 4, 3]) # Creates linked list for 342
l2 = createLinkedList([5, 6, 4]) # Creates linked list for 465

result = Solution.addTwoNumbers(l1, l2)

# Function to print the linked list
def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print() # for newline

printLinkedList(result) # Should print 7 0 8