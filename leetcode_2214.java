public class LRUCache {

	public static class Node {
		public Node pre;
		public Node next;
		public int val;
		public int key;

		public Node(int key, int val) {
			this.key = key;
			this.val = val;
			this.pre = this;
			this.next = this;
		}

		public void add(Node node) {
			Node nextNode = this.next;
			this.next = node;
			node.pre = this;
			node.next = nextNode;
			nextNode.pre = node;
		}

		public void remove() {
			Node preNode = this.pre;
			Node nextNode = this.next;
			preNode.next = nextNode;
			nextNode.pre = preNode;
		}
	}

	private Node list = new Node(-1, -1);
	private Map<Integer, Node> nodeMap = new HashMap<Integer, Node>();
	int capacity;

	public LRUCache(int capacity) {
		this.capacity = capacity;
	}

	public int get(int key) {
		Node node = nodeMap.get(key);
		if (node != null) {
			node.remove();
			list.add(node);
			return node.val;
		}
		return -1;
	}

	public void set(int key, int value) {
		Node node = nodeMap.get(key);
		if (node != null) {
			node.remove();
			node.val = value;
			list.add(node);
		} else {
			if (nodeMap.keySet().size() == capacity) {
				Node last = list.pre;
				last.remove();
				nodeMap.remove(last.key);
			}
			node = new Node(key, value);
			list.add(node);
			nodeMap.put(key, node);
		}
	}

}
