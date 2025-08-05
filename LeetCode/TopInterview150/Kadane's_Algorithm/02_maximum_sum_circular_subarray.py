class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    total_sum = sum(nums)

    max_sum = current_max = nums[0]
    min_sum = current_min = nums[0]

    for num in nums[1:]:
      current_max = max(num, current_max + num)
      max_sum = max(max_sum, current_max)

      current_min = min(num, current_min + num)
      min_sum = min(min_sum, current_min)

    if max_sum < 0:
      return max_sum

    return max(max_sum, total_sum - min_sum)
