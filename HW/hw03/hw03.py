HW_SOURCE_FILE = 'hw03.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    #def iter_helper(n, g1, g2, g3):
    gn = []
    for i in range(1, 4):
        gn.append(i)

    #print(gn)
    if n <= 3:
        return n
    else:
        i = 4
        while i <= n:
            gi = gn[i-2] + 2*gn[i-3] + 3*gn[i-4]
            gn.append(gi)

            i += 1
    #print(gn)
    return gn[n-1]

def g_iter2(n):
    # sol
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    from operator import add, sub

    def recur(i, res, fn):
        #print('a', i, res, fn == add)
        if i > n:
            return res
        if i != 0 and (i % 7 == 0 or has_seven(i)):
            if fn == add:
                return recur(i + 1, fn(res, 1), sub)
            else:
                return recur(i + 1, fn(res, 1), add)
        else:
            return recur(i + 1, fn(res, 1), fn)

    return recur(1, 0, add)

    '''
    i = 1
    res = 0
    fn = add

    while i <= n:
        #print('a0', i, res)
        if i != 0 and (i % 7 == 0 or has_seven(i)):
            #print('a', res, fn == add)
            res = fn(res, 1)
            if fn == add:
                #print('b')
                fn = sub
            else:
                fn = add
        else:
            res = fn(res, 1)
        i += 1
    return res
    '''

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def find_max_sub(amount):
        """Find the max nuber that is a power of 2 and less than amount"""
        i = 1
        while i <= amount:
            #print(i)
            i = i * 2
        return i // 2


    def recur(amount, max_coin):
        if amount == 0:
            #print('b', amount, max_coin)
            return 1
        elif amount < 0:
            return 0
        elif max_coin == 0:
            return 0
        else:
            m = find_max_sub(max_coin)
            #print('a', amount, m)
            use_m = recur(amount - m, m)
            no_m = recur(amount, m // 2)

            return use_m + no_m

    m = find_max_sub(amount)

    return recur(amount, m)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    all_pos = [1, 2, 3]
    alter = [x for x in all_pos if x != start and x != end][0]

    if n == 1:
        print_move(start, end)
    else:
        move_stack(n - 1, start, alter)
        move_stack(1, start, end)
        move_stack(n - 1, alter, end)

    '''
    if n == 1:
        print_move(start, end)
    else:
        if n % 2 == 0: 
            print_move(start, alter)
            move_stack(n - 1, start, end)
            print_move(alter, end)
        else:
            print_move(start, end)
            #if n > 2:
            move_stack(n - 1, start, alter)
            print_move(end, alter)
        #move_stack(n - 1, start, end)
        #move_stack(n - 1, end, alter)
    '''

def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    if len(lst) < 1:
        return lst
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])

def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    res = []
    i = 0
    j = 0
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    while True:
        #print(i, j)
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
        if i == len(lst1):
            if j == len(lst2) - 1:
                res.append(lst2[j])
            else:
                res.extend([lst2[j:]])
            break
        elif j == len(lst2):
            if i == len(lst1) - 1:
                res += [lst1[i]]
            else:
                res += lst1[i:]
            break

    return res


def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"

###################
# Extra Questions #
###################

from operator import sub, mul

def Y(f):
    """The Y ("paradoxical") combinator."""
    return f(lambda: Y(f))


def Y_tester():
    """
    >>> tmp = Y_tester()
    >>> tmp(1)
    1
    >>> tmp(5)
    120
    >>> tmp(2)
    2
    """
    "*** YOUR CODE HERE ***"
    return Y(________)  # Replace 
