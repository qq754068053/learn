from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return "none"

        def getNodeVal(treeNode: TreeNode) -> str:
            if treeNode is None:
                return "none"
            return str(treeNode.val)

        values = []
        queue = deque()
        node = root
        while len(queue) != 0 or node is not None:
            values.append(getNodeVal(node))
            if node is not None:
                queue.append(node)
                node = node.left
            else:
                node = queue.pop()
                node = node.right
        values.append(getNodeVal(None))

        return '-'.join(values)

    def deserialize(self, data: str) -> TreeNode:
        # 初始化所有的节点, 包括None
        values = data.split("-")
        nodes = deque()
        for i in range(len(values)):
            if values[i] == "none":
                nodes.append(None)
            else:
                nodes.append(TreeNode(int(values[i])))

        root = nodes.popleft()

        stack = [root]
        while len(nodes) != 0:
            node = nodes.popleft()
            if stack[-1] is None:
                while stack[-1] is None:
                    stack.pop()
                stack[-1].right = node
                stack.pop()
            else:
                stack[-1].left = node
            stack.append(node)

        return root
