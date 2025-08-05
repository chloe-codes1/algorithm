class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        idx1 = m - 1
        idx2 = n - 1
        merged_idx = m + n -1

        while m >= 0 and n > 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[merged_idx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[merged_idx] = nums2[idx2]

                idx2 =- 1
            
            merged_idx -= 1
        
        nums1[:n] = nums2[:n]
