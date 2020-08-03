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

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, item in enumerate(nums):
            exclude_index = index
            for search_index, search_item in enumerate(nums):
                # compare only if not on current index
                if search_index != exclude_index:
                    if item + search_item == target:
                        index_list = [search_index, index]
        return index_list
# In[main]


nums = [2, 7, 11, 15]
s = Solution()

print(s.twoSum(nums, 9))


