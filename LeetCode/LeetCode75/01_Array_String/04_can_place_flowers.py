"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List

# Time Complexity: O(N), Space Complexity: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        for i, availability in enumerate(flowerbed):
            is_empty = availability == 0
            is_left_empty = (i == 0 or flowerbed[i - 1] == 0)
            is_right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

            if is_empty and is_left_empty and is_right_empty:
                count += 1
                flowerbed[i] = 1

                if count == n:
                    return True

        return count >= n

solution = Solution()
result = solution.canPlaceFlowers([1,0,0,0,1], 1)
print("Result:", result)
