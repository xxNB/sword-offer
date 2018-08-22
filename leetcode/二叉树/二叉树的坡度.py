class Solution:
    res = 0
    def findTilt(self, root):
        self.postorder(root)
        return self.res

    def postorder(self, node):
        if not node:
            return 0
        leftSum = self.postorder(node.left)
        rightSum = self.postorder(node.right,)
        self.res += abs(leftSum-rightSum)
        return leftSum+rightSum+node.val