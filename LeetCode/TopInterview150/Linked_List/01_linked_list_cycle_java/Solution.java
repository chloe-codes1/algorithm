/*
Definition for singly-linked list.
class ListNode {
  int val;
  ListNode next;
  ListNode(int x) {
	  val = x;
	  next = null;
  }
}
 */

public class Solution {

	public boolean hasCycle(ListNode head) {
		if (head == null) {
			return false;
		}

		ListNode slow = head;
		ListNode fast = head;

		while (fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;

			if (slow == fast) {
				return true;
			}
		}

		return false;
	}

	static class ListNode {

		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
			next = null;
		}
	}

	public static void main(String[] args) {
		Solution solution = new Solution();

		// Test 1: No cycle
		ListNode a = new ListNode(1);
		ListNode b = new ListNode(2);
		ListNode c = new ListNode(3);
		a.next = b;
		b.next = c;
		System.out.println("Test 1 (no cycle): " + solution.hasCycle(a)); // false

		// Test 2: Cycle back to head
		c.next = a;
		System.out.println("Test 2 (cycle to head): " + solution.hasCycle(a)); // true

		// Test 3: Single node, no cycle
		ListNode single = new ListNode(10);
		System.out.println("Test 3 (single node no cycle): " + solution.hasCycle(single)); // false

		// Test 4: Single node, cycle to itself
		single.next = single;
		System.out.println("Test 4 (single node self cycle): " + solution.hasCycle(single)); // true

		// Test 5: null input
		System.out.println("Test 5 (null input): " + solution.hasCycle(null)); // false
	}
}


