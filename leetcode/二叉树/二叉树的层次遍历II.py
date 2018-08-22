class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        q,result = [root], []
        while q:
            tmp = list()
            for _ in range(len(q)):
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.insert(0, tmp)
        return result
