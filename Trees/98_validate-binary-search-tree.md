problem : https://leetcode.com/problems/validate-binary-search-tree/description/
---

### ✅ Breakdown of How It Works:

```python
def isvalid(low, root, high):
    if root == None:
        return True
```

* Base case: If the node is `None`, it's valid — nothing to check.

```python
    if not low < root.val < high:
        return False
```

* Current node must lie **strictly between** the low and high bounds.
* If it breaks the BST rule, return `False`.

```python
    return isvalid(low, root.left, root.val) and isvalid(root.val, root.right, high)
```

* Recurse on:

  * Left child → upper bound becomes `root.val`
  * Right child → lower bound becomes `root.val`
* Combine with `and` to ensure **both** subtrees are valid.

---

### ✅ Final Touch — How to Call It:

Make sure to call like this **inside your main function**:

```python
return isvalid(float('-inf'), root, float('inf'))
```

So if this is your `isValidBST()` method in Leetcode:

```python
def isValidBST(self, root):
    def isvalid(low, root, high):
        if root == None:
            return True
        if not low < root.val < high:
            return False
        return isvalid(low, root.left, root.val) and isvalid(root.val, root.right, high)

    return isvalid(float('-inf'), root, float('inf'))
```

---

💡 This logic ensures:

* Every node is compared not just with its immediate parent
* But also with the **entire valid range** for its subtree
