Problem : https://leetcode.com/problems/binary-tree-level-order-traversal/

(It was breath first search- BFS as we check level by level)
1. always include base condition.
2. add root into queue first.
3. loop for parent node till end of the tree. then add its child left and right (dont forget to check if it is exist or not.) into queue by poping root node.
4. loop over for child nodes of every root node.
5. take empty level to store child nodes.
6. after every one iteration of both child nodes. append them into level



my mistakes:

1. i forgot to include base conditions.
2. looping for child nodes inside parent node loop.

```python
  if root == None:
      return 0

  depth = 0
  queue = []
  queue.append(root)
  while queue:
      for _ in range(len(queue)):
          node = queue.pop(0)
          if node.left != None:
              queue.append(node.left)
          if node.right != None:
              queue.append(node.right)
      depth += 1
  
  return depth


```
problem : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/ - Maximum depth of binary tress.

      - is exactly same but here instead of storing in level and result we just need to count of levels. 

  make sure previous problm we placed level inside root loop. for reseting for every child nodes.

- but here we need to count depth one by one so always make an eye to place count in beginning. not wihtin loops. and count after every new root node.


Depth first search(DFS) -

            1. recurse both child nodes till it end. and add 1 at every step because if was 0-indexed.


```python
if root == None:
      return 0

left = self.maxDepth(root.left)  
right = self.maxDepth(root.right)
return max(left,right)+1 #take maximum depth from both nodes
