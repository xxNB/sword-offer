class Solution:
    def tree2str(self, t):
        if not t:
            return ""
        res = ""
        res += str(t.val)
        if t.left:
            res+="("+self.tree2str(t.left)+")"
        elif t.right:
            res+="()"
        if t.right:
            res+="("+self.tree2str(t.right)+")"
        return res