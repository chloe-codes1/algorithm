class Solution {

	public int maxProfit(int[] prices) {
		int minPrice = Integer.MAX_VALUE;
		int maxProfit = 0;

		for (int price : prices) {
			minPrice = Math.min(price, minPrice);
			maxProfit = Math.max(price - minPrice, maxProfit);
		}

		return maxProfit;
	}

	public static void main(String[] args) {
		var solution = new Solution();
		System.out.println("Solution: " + solution.maxProfit(new int[]{7, 1, 5, 3, 6, 4})); // 5
	}
}