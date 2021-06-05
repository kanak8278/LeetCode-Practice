# We could use memoization if every test case contains a number of input. But if before every test_case
# class is reinitialized then memoization of no use.

# This problem can be solved using CATLAN NUMBER formula, which would give result in O(0)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def countTrees(n):
            count = 0
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n == 2:
                return 2
            else:
                for i in range(1, n + 1):
                    count += (countTrees(n - i) * countTrees(i - 1))
                # print(count)
                return count

        if n == 0:
            return 0
        return countTrees(n)



