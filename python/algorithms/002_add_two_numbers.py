#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:08:12 2019

@author: brandon

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # add
        n3 = l1.val + l2.val
        # store
        l3 = ListNode(n3)
        # break into val and carry if over 9
        if l3.val > 9:
            carry = 1
            l3.val = int(list(str(l3.val))[1])
        else:
            carry = 0
        # base case
        if l1.next is not None and l2.next is not None:  # even length lists
            # giving carry value to either node value works
            l1.next.val = l1.next.val + carry
            # recursive call joins nodes
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        elif l1.next is None and l2.next is None:  # last addition, even lists
            if carry == 1:
                l3.next = ListNode(1)
        elif l1.next is None:  # l1 list shorter than l2
            l3.next = self.addTwoNumbers(ListNode(0 + carry), l2.next)
        elif l2.next is None:  # l2 list shorter than l1
            l3.next = self.addTwoNumbers(l1.next, ListNode(0 + carry))
        return l3

    def print_node(self, l1: ListNode):
        while l1 is not None:
            print(l1.val)
            l1 = l1.next
        print('\n')

# In[main]


l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

s = Solution()
l3 = s.addTwoNumbers(l1_1, l2_1)
print('Test case: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)')
s.print_node(l3)

l1_1 = ListNode(5)
l2_1 = ListNode(5)
l3 = s.addTwoNumbers(l1_1, l2_1)
print('Test case: (5) + (5) = (0 -> 1)')
s.print_node(l3)

l1_1 = ListNode(1)
l1_2 = ListNode(8)
l1_1.next = l1_2

l2_1 = ListNode(0)
l3 = s.addTwoNumbers(l1_1, l2_1)
print('Test case: (1 -> 8) + (0) = (1 -> 8)')
s.print_node(l3)

l1_1 = ListNode(9)
l1_2 = ListNode(8)
l1_1.next = l1_2
l2_1 = ListNode(1)
l3 = s.addTwoNumbers(l1_1, l2_1)
print('Test case: (9 -> 8) + (1) = (0 -> 9)')
s.print_node(l3)