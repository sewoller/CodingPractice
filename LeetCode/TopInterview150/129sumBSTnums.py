def sumNumbers(self, root: Optional[TreeNode]) -> int:
    dfs_results = []
    def dfs(root, current_val):
        if not root: return 0
        current_val = 10*current_val + root.val
        if not root.left and not root.right:
            dfs_results.append(current_val)
        dfs(root.left, current_val)
        dfs(root.right, current_val)
    dfs(root, 0)
    answer = 0
    for i in dfs_results:
        answer += i
    return answer