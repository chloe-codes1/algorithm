import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {

	public int[] twoSum(int[] nums, int target) {
		Map<Integer, Integer> options = new HashMap<>();

		for (var i = 0; i < nums.length; i++) {
			int candidate = target - nums[i];
			if (options.containsKey(candidate)) {
				return new int[]{options.get(candidate), i};
			}

			options.put(nums[i], i);
		}

		return new int[]{};
	}

	public static void main(String[] args) {
		Solution solution = new Solution();

		// 테스트 케이스 1
		int[] nums1 = {2, 7, 11, 15};
		int target1 = 9;
		System.out.println("Test 1: " + Arrays.toString(solution.twoSum(nums1, target1))); // [0, 1]

		// 테스트 케이스 2
		int[] nums2 = {3, 2, 4};
		int target2 = 6;
		System.out.println("Test 2: " + Arrays.toString(solution.twoSum(nums2, target2))); // [1, 2]

		// 테스트 케이스 3
		int[] nums3 = {3, 3};
		int target3 = 6;
		System.out.println("Test 3: " + Arrays.toString(solution.twoSum(nums3, target3))); // [0, 1]

		// 테스트 케이스 4 - 없는 경우
		int[] nums4 = {1, 2, 3};
		int target4 = 7;
		System.out.println("Test 4: " + Arrays.toString(solution.twoSum(nums4, target4))); // []
	}
}
