# Q1
def abundant(n):
    """Print all ways of forming positive integer n by multiplying two positive
    integers together, ordered by the first term. Then, return whether the sum
    of the proper divisors of n is greater than n.

    A proper divisor of n evenly divides n but is less than n.

    >>> abundant(12) # 1 + 2 + 3 + 4 + 6 is 16, which is larger than 12
    1 * 12
    2 * 6
    3 * 4
    True
    >>> abundant(14) # 1 + 2 + 7 is 10, which is not larger than 14
    1 * 14
    2 * 7
    False
    >>> abundant(16)
    1 * 16
    2 * 8
    4 * 4
    False
    >>> abundant(20)
    1 * 20
    2 * 10
    4 * 5
    True
    >>> abundant(22)
    1 * 22
    2 * 11
    False
    >>> r = abundant(24)
    1 * 24
    2 * 12
    3 * 8
    4 * 6
    >>> r
    True

    """
    i = 1
    res = []
    while i * i <= n:
        if n % i == 0:
            print(i, '*', n//i)
            res.extend([i, n//i])
        i += 1
    res.remove(n)
    res.remove(1)
    res = set(res)
    if sum(res) > n:
        return True
    else:
        return False

# Q2
def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    n = a
    while n != 1:
        if n == b:
            return True
        if n % 2 == 0:
            n = n/2
        else:
            n = n * 3 + 1

    # Then try b
    n = b
    while n != 1:
        if n == a:
            return True
        if n % 2 == 0:
            n = n/2
        else:
            n = n * 3 + 1
    
    return False

# Q3
def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> identity = lambda x: x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    return lambda x: f(x) if x < b else g(x)

# Q4
def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x+dx) + f(x) + f(x - dx))/3

def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f

    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    return repeated(lambda g: smooth(g, dx), n)(f)

def repeated(f, n):
    """Returns a single-argument function that takes a value, x, and applies
    the single-argument function F to x N times.
    >>> repeated(lambda x: x*x, 3)(2)
    256
    """
    def h(x):
        for k in range(n):
            x = f(x)
        return x
    return h

# Q6
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: 10*y + x % 10
    while x > 0:
        x, y = x // 10, f()
        #print(x, y)
    return y == n

# Q7
def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list.
    >>> deep_len(link(1, link(2, link(3, empty))))
    3
    >>> deep_len(link(link(1, link(2, empty)), link(3, link(4, empty))))
    4
    >>> deep_len(link(link(link(1, link(2, empty)), \
            link(3, empty)), link(link(4, empty), link(5, empty))))
    5
    """
    if not is_link(lnk):
        return 1

    if lnk == empty:
        return 0

    #if is_link(lnk):
    return deep_len(first(lnk)) + deep_len(rest(lnk))

# Q8
def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings.

    >>> marvins_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> brians_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = link(1, link(2, link(3, link(4, empty))))
    >>> marvins_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> marvins_to_string(empty)
    '[]'
    >>> brians_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> brians_to_string(empty)
    '()'
    """
    # This won't work for nested linked list
    def rep(lnk):
        if lnk == empty:
            return empty_repr
        return front + str(first(lnk)) + mid + rep(rest(lnk)) + back

    return rep

# Q9
def tree_map(fn, t):
    """Maps the function fn over the entries of tree and returns the
    result in a new tree.

    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    """
    if is_tree(t):
        first = entry(t)
        return tree(fn(first), [tree_map(fn, t) for t in children(t)])

# Q10
def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if not t1:
        return t2
    if not t2:
        return t1
    new_entry = entry(t1) + entry(t2)
    t1_children, t2_children = children(t1), children(t2)
    length_t1, length_t2 = len(t1_children), len(t2_children)
    if length_t1 < length_t2:
        t1_children += [None for _ i range(length_t1, length_t2)]
    if length_t2 < length_t1:
        t2_children += [None for _ i range(length_t2, length_t1)]
    return tree(new_entry, [add_trees(child1, child2) for child1, child2 in zip(t1_children, t2_children)])

# Linked List definition
empty = 'empty'


def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))


def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]


def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]


def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]


def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

# Tree ADT
def tree(entry, children=[]):
    for child in children:
        assert is_tree(child), 'children must be trees'
    return [entry] + list(children)


def entry(tree):
    return tree[0]


def children(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for child in children(tree):
        if not is_tree(child):
            return False
    return True


def is_leaf(tree):
    return not children(tree)


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


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(entry(t), [copy_tree(child) for child in children(t)])