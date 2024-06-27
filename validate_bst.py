
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not root:
                return True 

            if node.val >= high or node.val <= low:
                print("false hit")
                return False 

            if node.left:
                if not validate(node.left, low, node.val):
                    return False
        
            if node.right:
                if not validate(node.right, node.val, high):
                    return False

            return True 

        return validate(root, -math.inf, math.inf)




'''
   5
  / \ 
 1   4
    / \
   3   6