class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def _get_height(root):
    if root is None:
        return 0
    return root.height

def _get_balance(root):
    if root is None:
        return 0
    return _get_height(root.left) - _get_height(root.right)

def _rotate_left(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(_get_height(z.left), _get_height(z.right))
    y.height = 1 + max(_get_height(y.left), _get_height(y.right))

    return y

def _rotate_right(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(_get_height(z.left), _get_height(z.right))
    y.height = 1 + max(_get_height(y.left), _get_height(y.right))

    return y

def _get_min_value_node(root):
    if root is None or root.left is None:
        return root
    return _get_min_value_node(root.left)

def delete(root, key):
    if root is None:
        return root
    elif key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            temp = _get_min_value_node(root.right)
            root.key = temp.key
            root.right = delete(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(_get_height(root.left), _get_height(root.right))
    balance = _get_balance(root)

    if balance > 1:
        if _get_balance(root.left) >= 0:
            return _rotate_right(root)
        else:
            root.left = _rotate_left(root.left)
            return _rotate_right(root)
    elif balance < -1:
        if _get_balance(root.right) <= 0:
            return _rotate_left(root)
        else:
            root.right = _rotate_right(root.right)
            return _rotate_left(root)

    return root