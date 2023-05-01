""" How to count the hight of a binary tree
 1. if current node is leaf, count 0
 2. count ++ every time from a child node to its parent node
 3. if a node has both left and right heigh, only choose the max to prune the counting
 """

def height(root):
  if root.left is None and root.right is None:    # leaf
    return 0
  elif root.left is None:       # left is None, only track right
    return height(root.right) +1 
  elif root.right is None:      # right is None, only track left
    return height(root.left) + 1
  else:                 # choose max from left and right to prune
    return max( height(root.left) +1, height(root.right) +1)
