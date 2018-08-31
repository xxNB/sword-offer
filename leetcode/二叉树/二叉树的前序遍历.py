



class Solution:
    # stack = []
    # def preorderTraversal(self, root):
    #     self.stack.append(root)
    #     self.preorderTraversal(root.left)
    #     self.preorderTraversal(root.right)
    def preorderTraversal(self, root):
        stack = [root]
        res = []
        node = root
        while node or stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res