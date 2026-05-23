# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = deque([p])
        tree2 = deque([q])

        while tree1 and tree2:
            for i in range(len(tree1)):
                node1, node2 = tree1.popleft(), tree2.popleft()

                if node1 is None and node2 is None:
                    continue
                if node1 is None or node2 is None or node1.val != node2.val:
                    return False
                tree1.append(node1.right)
                tree1.append(node1.left)
                tree2.append(node2.right)
                tree2.append(node2.left)


            

        return True
        


         