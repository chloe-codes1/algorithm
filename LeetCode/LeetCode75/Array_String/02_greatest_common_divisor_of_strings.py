"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

# Time Complexity: O(N + M + log(min(N, M))), Space Complexity: O(N+M)

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1: int = len(str1)
        len_str2: int = len(str2)
        
        gcd_length = gcd(len_str1, len_str2)
        candidate = str1[:gcd_length]
        
        if str1 == candidate * (len_str1 // gcd_length) and str2 == candidate * (len_str2 // gcd_length):
            return candidate
        
        return ""

solution = Solution()
# result = solution.gcdOfStrings("ABCDEF", "ABC")
result = solution.gcdOfStrings("ABCABC", "ABC")
print("Result:", result)
