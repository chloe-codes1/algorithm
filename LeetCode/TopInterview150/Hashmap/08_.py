class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for idx, num in enumerate(nums):
            if num in last_index and idx - last_index[num] <= k:
                return True
            last_index[num] = idx
        
        return False



from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()  
        
        for idx, num in enumerate(nums):
            if num in window:
                return True
            
            window.add(num)

            if len(window) > k:
                window.remove(nums[idx - k])
        
        return False
