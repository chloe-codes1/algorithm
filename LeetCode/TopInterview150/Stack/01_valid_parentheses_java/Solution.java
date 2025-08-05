import java.util.Map;
import java.util.Stack;

class Solution {

	public boolean isValid(String s) {
		Map<Character, Character> mapping = Map.of(
			'(', ')',
			'{', '}',
			'[', ']'
		);
		Stack<Character> stack = new Stack<>();
		for (char c : s.toCharArray()) {
			if (mapping.containsKey(c)) {
				stack.push(mapping.get(c));
			} else {
				if (stack.empty() || stack.pop() != c) {
					return false;
				}
			}
		}
		return stack.isEmpty();
	}
}