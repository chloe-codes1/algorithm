class Solution {

	public int maxSubarraySumCircular(int[] nums) {
		int totalSum = 0;

		int maxSum = Integer.MIN_VALUE, currentSum = 0;
		int minSum = Integer.MAX_VALUE, currentMin = 0;

		for (var num : nums) {
			totalSum += num;

			currentSum = Math.max(num, currentSum + num);
			maxSum = Math.max(currentSum, maxSum);

			currentMin = Math.min(num, currentMin + num);
			minSum = Math.min(currentMin, minSum);
		}

		return maxSum < 0 ? maxSum : Math.max(maxSum, totalSum - minSum);
	}

	public static void main(String[] args) {
		var solution = new Solution();
		System.out.println(
			"Solution 1: " + solution.maxSubarraySumCircular(new int[]{1, -2, 3, -2}));
	}
}