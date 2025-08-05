from typing import List

# Time Complexity: O(n log n), Space Complexity: O(1)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for idx, citation in enumerate(citations):
            if citation < idx + 1:
                return idx
        return len(citations)
