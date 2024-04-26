class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        root_index = inorder.index(root_val)
        
        left_sub_inorder = inorder[:root_index]
        right_sub_inorder = inorder[root_index + 1:]
        
        preorder = preorder[1:]
        
        if left_sub_inorder:
            root.left = self.buildTree(preorder[:len(left_sub_inorder)], left_sub_inorder)
        
        if right_sub_inorder:
            root.right = self.buildTree(preorder[len(left_sub_inorder):],right_sub_inorder)
        
        return root

        