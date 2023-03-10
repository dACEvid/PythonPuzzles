# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = result = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            curr_val = carry
            if l1:
                curr_val += l1.val
                l1 = l1.next
            if l2:
               curr_val += l2.val
               l2 = l2.next

            result.next = ListNode(curr_val % 10)
            result = result.next

            carry = 1 if curr_val >= 10 else 0

        return root.next


if __name__ == '__main__':
    l1 = ListNode() # first ListNode provided
    l2 = ListNode() # second ListNode provided
    solution = Solution()
    solution.addTwoNumbers(l1, l2)