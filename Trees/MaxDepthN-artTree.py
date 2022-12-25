'''
    Leetcode-559---> Maximum Depth of N-ary Tree
    Given a n-ary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.
'''
class Node:
    def __init__(self,value=None,children=None):
        self.val = value
        self.children = children

#Copy the below code in Leetcode         
class Solution:
    def maxDepth(self,root: 'Node') -> int:
        if root == None:
            return 0
        #We need to check all the children of the root
        depth = 0
        for node in root.children:
            print("Node=",node.val)
            childrenDepth = self.maxDepth(node)
            depth = max(depth,childrenDepth)
        return depth + 1
    
# if __name__ == "__main__":
#     #Construct a tree
#     root = Node(1,(Node(3,(Node(5,None),Node(6,None))),Node(2,None),Node(4,None)))
#     #construct obj for solution class
#     obj = Solution()
#     print("Max Depth of N-ary Tree: ", obj.maxDepth(root))