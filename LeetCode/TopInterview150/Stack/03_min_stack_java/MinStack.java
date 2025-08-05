import java.util.Stack;

class MinStack {

	private final Stack<Integer> stack;
	private final Stack<Integer> minStack;

	public MinStack() {
		stack = new Stack<>();
		minStack = new Stack<>();
	}

	public void push(int val) {
		stack.push(val);
		if (minStack.empty() || minStack.peek() >= val) {
			minStack.push(val);
		}
	}

	public void pop() {
		var val = stack.pop();
		if (!minStack.empty() && minStack.peek().equals(val)) {
			minStack.pop();
		}
	}

	public int top() {
		return stack.peek();
	}

	public int getMin() {
		return minStack.peek();
	}

	public static void main(String[] vars) {
		MinStack obj = new MinStack();
		obj.push(-2);
		obj.push(0);
		obj.push(-4);

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
