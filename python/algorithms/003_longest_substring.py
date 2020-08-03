# -*- coding: utf-8 -*-

"""
Created on Wed Jul 17 12:27:16 2019
@author: KNOXB

Given a string, find the length of the longest substring without 
repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence
             and not a substring.

"""

 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        a substring will be created with the current non-repeating chars
        '''
        substring_list = []
        substring = ''

        # check if string is null
        if s is None:
            print('Specify a non-empty string')
            return 0

        # import pdb; pdb.set_trace()
        for sub in s:
            # read in next character, and see if it exists in substring
            if sub in substring:
                # add current substring to substring array
                # if next character does match, replace substring with current character
                substring_list.append(substring)
                # TODO: this needs to shave off entries, not start over
                # must remove everything from the start of the string to first
                # occurance of current char
                # use split?
                # substring = sub
                substring = substring.split(sub, 1)[1]
            else:
                # if next character does not match add to substring
                substring = substring + sub

        # log last substring
        substring_list.append(substring)
        # calculate longest string in substring_list
        length = 0
        if substring_list is not None:
            for sub in substring_list:
                if len(sub) > length:
                    # final_string = sub
                    length = len(sub)
        # print(final_string)
        return length 

# test cases
s = Solution()

print('Example 6')
print(str(s.lengthOfLongestSubstring('dvdf')) + '\n')

print('Example 1')
print(str(s.lengthOfLongestSubstring('abcabcbb')) + '\n')

print('Example 2')
print(str(s.lengthOfLongestSubstring('bbbbb')) + '\n')

print('Example 3')
print(str(s.lengthOfLongestSubstring('pwwkew')) + '\n')

print('Example 4')
print(str(s.lengthOfLongestSubstring(' ')) + '\n')

print('Example 5')
print(str(s.lengthOfLongestSubstring('au')) + '\n')