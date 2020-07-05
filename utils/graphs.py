from typing import List


class BiNode:
    val: int = None
    left = None
    right = None

    def __str__(self):
        return f"({self.left if self.left else '_' }/{self.val}\\{self.right if self.right else '_'})"

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BiPaNode(BiNode):
    parent = None


def ltbt(arr: List[int]) -> BiNode:
    return list_to_binary_tree(arr)


def list_to_binary_tree(arr: List[int]) -> BiNode:
    nodes = [BiPaNode(arr[0])]
    for i in range(1, len(arr)):
        parent = nodes[(i - 1)//2]

        if not parent and arr[i]:
            raise Exception(f"Cannot have children without parents to attach to,"
                            f" for {arr[i]} on input {arr}")

        if not arr[i]:
            nodes.append(None)
        else:
            node_now = BiPaNode(arr[i])
            node_now.parent = parent

            nodes.append(node_now)
            if (i-1) % 2:
                parent.right = node_now
            else:
                parent.left = node_now

    return nodes[0]


def get_node_by_val(root: BiNode, target):
    if not root:
        return None
    if root.val == target:
        return root
    else:
        return get_node_by_val(root.left, target) \
            or get_node_by_val(root.right, target)
