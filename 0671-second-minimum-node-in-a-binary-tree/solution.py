class Solution:
    def findSecondMinimumValue(self, root):
        values = set()

        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        values = sorted(values)

        if len(values) < 2:
            return -1

        return values[1]
