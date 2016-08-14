def tree(entry, children=[]):
    return [entry] + list(children)

def entry(tree):
    return tree[0]

def children(tree):
    return tree[1:]

def is_leaf(tree):
    return not children(tree)

def height(t):
    if is_leaf(t):
        return 0
    return 1 + max([height(subtree) for subtree in children(t)])

def tree_size(t):
    return 1 + sum([tree_size(child) for child in children(t)])

def find_path(tree, x):
    if entry(tree) == x:
        return [entry(tree)]
    node, trees = entry(tree), children(tree)
    for path in [find_path(t, x) for t in trees]:
        if path:
            return [node] + path

def prune(t, k):
    '''
    Return a new tree that has the top k levels
    '''
    if k == 0:
        return tree(entry(t), [])
    else:
        return tree(entry(t), [prune(child, k - 1) for child in children(t)]

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the entry.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(entry(t)))
    for child in children(t):
        print_tree(child, indent + 1)

