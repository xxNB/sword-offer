class Solution:
    def helper(self,root,orders,res):
        if root is None:
            return "#"
        my_order = str(root.val)+','+self.helper(root.left,orders,res)+','+self.helper(root.right, orders, res)
        if orders.get(my_order, 0)==1:
            res.append(root)
        if my_order in orders:
            orders[my_order]+=1
        else:
            orders[my_order]=1
        return my_order

    def findDuplicateSubtrees(self,root):
        """
        <后序遍历>,还有数组序列化，建立序列化跟其出现次数的映射
        :param root:
        :return:
        """
        orders = dict()
        res = list()
        self.helper(root,orders,res)
        return res