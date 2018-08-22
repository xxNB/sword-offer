package leetcode;

/**
 * Created by zhangxin on 2018/8/10.
 */
public class lowestCommonAncestorOfaBonarySearchTree {
    public TreeNode lowestCommonAncestorOfaBonarySearchTree(TreeNode root, TreeNode p, TreeNode q) {

        while((root.val-p.val)*(root.val-q.val)>0)
            root=p.val<root.val?root.left:root.right;
        return root;

    }
}