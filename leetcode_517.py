class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        stack = []
        if root is not None:
            stack.append(root)
        while len(stack) > 0:
            p = stack[len(stack) - 1]
            if p.left is not None:
                stack.append(p.left)
                p.left = None
            else:
                result.append(stack.pop().val)                
                if p.right is not None:
                    stack.append(p.right)
        return result




s = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(7)
root.left.right = TreeNode(8)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(5)
print s.inorderTraversal(root)
