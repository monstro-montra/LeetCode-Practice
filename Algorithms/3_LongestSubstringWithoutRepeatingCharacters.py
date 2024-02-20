'''
Given a string s, find the length of the longest 
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, string: str) -> (str, int): # return a string and an int
        # store the position of characters
        characterIndexMap = {}
        start = maxLength = 0
        longestSubstring = ""

        for i, character in enumerate(string): # for each character in the string 
            # If character is already in dictionary and its index is within the current substring
            if character in characterIndexMap and characterIndexMap[character] >= start:
                # update start to the next character after the last occurence.
                start = characterIndexMap[character] + 1

            # update the last position of the character
            characterIndexMap[character] = i

            # update maxLength and longestSubstring if the current substring is longer than maxLength
            if i - start + 1 > maxLength:
                maxLength = i - start + 1
                longestSubstring=string[start:i+1]

        return longestSubstring, maxLength



if __name__ == "__main__":
    solution = Solution() # init a variable called solution and set it to the Solution class.
    s = "abcabcbb" 

    substr, length = solution.lengthOfLongestSubstring(s)

    print(f"Longest substring without repeating characters: '{substr}' with length {length}")
