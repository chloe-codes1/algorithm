"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

from typing import Iterator

# Time Complexity: O(N), Space Complexity: O(N)
# Two pointer로 다시 풀기

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: set[str] = set("aeiouAEIOU") 
        s_list: list[str] = list(s)  
        candidates: list[str] = [char for char in s if char in vowels]  

        candidates: Iterator[str] = iter(candidates[::-1])
        for i, char in enumerate(s_list):
            if char in vowels:
                s_list[i] = next(candidates)

        return ''.join(s_list)
        
        
solution = Solution()
result = solution.reverseVowels("IceCreAm")
print(result)
