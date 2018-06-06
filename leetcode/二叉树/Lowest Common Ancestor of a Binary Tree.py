"""
88. Lowest Common Ancestor of a Binary Tree
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    后序遍历二叉树，得到从根节点到目标节点的“路径”，两条路径公共部分的末尾节点即为LCA

    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, p, q):
        pathP, pathQ = self.findPath(root, p), self.findPath(root, q)
        lenP, lenQ = len(pathP), len(pathQ)
        ans, x = None, 0
        while x < min(lenP, lenQ) and pathP[x] == pathQ[x]:
            ans, x = pathP[x], x + 1
        return ans

    def findPath(self, root, target):
        # 找出root节点到target节点的这段"距离"
        stack = []
        lastVisit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                # 最左边的节点 peek
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    # stack最右边的节点
                    lastVisit = stack.pop()
                    root = None
        return stack
