from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges: List[str] = []
        total = len(nums)
        current_index = 0
        
        while current_index < total:
            start_index = current_index
            end_index = current_index
            
            while end_index + 1 < total and nums[end_index + 1] == nums[end_index] + 1:
                end_index += 1
            
            if start_index == end_index:
                ranges.append(str(nums[start_index]))
            else:
                ranges.append(f"{nums[start_index]}->{nums[end_index]}")
            
            current_index = end_index + 1
        
        return ranges
