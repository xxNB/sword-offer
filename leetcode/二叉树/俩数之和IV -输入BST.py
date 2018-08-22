
class Solution:
    def findTarget(self, root, k):
        """
        刷题不知 twonum 刷遍leetcode也枉然

        :param root:
        :param k:
        :return:
        """
        if not root:
            return False

        bfs, s  = [root], set()
        for i in bfs:
            if k-i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False