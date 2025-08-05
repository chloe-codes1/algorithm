class Solution {

	public int maxSubArray(int[] nums) {
		int maxSum = nums[0];
		int currentSum = nums[0];

		for (int i = 1; i < nums.length; i++) {
			currentSum = Math.max(nums[i], nums[i] + currentSum);
			maxSum = Math.max(currentSum, maxSum);
		}

		return maxSum;
	}

	public static void main(String[] args) {
		Solution solution = new Solution();
		System.out.println(
			"Solution 1: " + solution.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
	}
}