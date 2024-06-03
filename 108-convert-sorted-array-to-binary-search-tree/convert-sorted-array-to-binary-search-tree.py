class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        queue = deque([(root, 0, mid - 1), (root, mid + 1, len(nums) - 1)])
        
        while queue:
            parent, left, right = queue.popleft()
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(nums[mid])
                if nums[mid] < parent.val:
                    parent.left = node
                else:
                    parent.right = node
                queue.append((node, left, mid - 1))
                queue.append((node, mid + 1, right))
        
        return root
