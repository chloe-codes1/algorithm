import java.util.Stack;

class ImprovedMinStack {

	private final Stack<Integer> stack = new Stack<>();
	private final Stack<Pair> minStackPair = new Stack<>();

	public void push(int val) {
		stack.push(val);
		if (minStackPair.empty() || minStackPair.peek().first() > val) {
			minStackPair.push(new Pair(val, 1));
		} else if (minStackPair.peek().first() == val) {
			var popped = minStackPair.pop();
			minStackPair.push(new Pair(popped.first(), popped.second() + 1));
		}
	}

	public void pop() {
		int val = stack.pop();
		if (val == minStackPair.peek().first()) {
			Pair minPair = minStackPair.pop();
			if (minPair.second() > 1) {
				minStackPair.push(new Pair(minPair.first(), minPair.second() - 1));
			}
		}
	}

	public int top() {
		return stack.peek();
	}

	public int getMin() {
		return minStackPair.peek().first();
	}

	record Pair(int first, int second) {

	}

	public static void main(String[] args) {
		ImprovedMinStack obj = new ImprovedMinStack();
		obj.push(5);
		obj.push(8);
		obj.push(1);

		System.out.println("minimum value of stack: " + obj.getMin());
		obj.pop();
		System.out.println("top value of stack: " + obj.top());
		System.out.println("minimum value of stack: " + obj.getMin());
	}
}

/**
 * Your MinStack object will be instantiated and called as such: MinStack obj = new MinStack();
 * obj.push(val); obj.pop(); int param_3 = obj.top(); int param_4 = obj.getMin();
 */