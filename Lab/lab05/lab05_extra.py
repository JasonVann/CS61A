"""Optional program for lab05 """

from lab05 import *

def sum_linked_list(lst, fn):
    """Applies a function FN to each number in LST and returns the sum
    of the resulting values

    >>> square = lambda x: x * x
    >>> double = lambda y: 2 * y
    >>> lst1 = link(1, link(2, link(3, link(4))))
    >>> sum_linked_list(lst1, square)
    30
    >>> lst2 = link(3, link(5, link(4, link(10))))
    >>> sum_linked_list(lst2, double)
    44
    """
    res = 0
    
    while lst != empty and first(lst) != empty:
        res += fn(first(lst))
        lst = rest(lst)
    return res

def change(lst, s, t):
    """Returns a link matching lst but with all instances of s 
    replaced by t. If s does not appear in lst, then return lst

    >>> lst = link(1, link(2, link(3)))
    >>> new = change(lst, 3, 1)
    >>> print_link(new)
    1 2 1
    >>> newer = change(new, 1, 2)
    >>> print_link(newer)
    2 2 2
    >>> newest = change(newer, 5, 1)
    >>> print_link(newest)
    2 2 2
    """
    if lst == empty:
        return lst
    else:
        #print('a', first(lst), rest(lst))
        if first(lst) == s:
            #print('b', s, rest(lst))
            return link(t, change(rest(lst), s, t))
        else:
            return link(first(lst), change(rest(lst), s, t))


def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    if linked_lst == empty:
        return []
    else:
        return [first(linked_lst)] + link_to_list(rest(linked_lst))

def insert(lst, item, index):
    """Returns a link matching lst but with the given item inserted at the
    specified index. If the index is greater than the current length, the item
    is appended to the end of the list.

    >>> lst = link(1, link(2, link(3)))
    >>> new = insert(lst, 9001, 1)
    >>> print_link(new)
    1 9001 2 3
    >>> newer = insert(new, 9002, 15)
    >>> print_link(newer)
    1 9001 2 3 9002
    """
    #print('a', index, lst)
    if index >= 0 and lst == empty:
        return link(item, empty)
    elif index == 0:
        return link(item, lst)
    else:
        return link(first(lst), insert(rest(lst), item, index - 1))

def interleave(s0, s1):
    """Interleave linked lists s0 and s1 to produce a new linked
    list.

    >>> evens = link(2, link(4, link(6, link(8, empty))))
    >>> odds = link(1, link(3, empty))
    >>> print_link(interleave(odds, evens))
    1 2 3 4 6 8
    >>> print_link(interleave(evens, odds))
    2 1 4 3 6 8
    >>> print_link(interleave(odds, odds))
    1 1 3 3
    """
    if s0 == empty:
        return s1
    elif s1 == empty:
        return s0

    return link(first(s0), link(first(s1), interleave(rest(s0), rest(s1))))

# Iterative version
# Sol from webpage
def interleave_iter(s0, s1):
    interleaved = empty
    while s0 != empty and s1 != empty:
        interleaved = link(first(s1), link(first(s0), interleaved))
        s0, s1 = rest(s0), rest(s1)
    remaining = s1 if s0 == empty else s0
    while remaining != empty:
        interleaved = link(first(remaining), interleaved)
        remaining = rest(remaining)
    return reverse_iterative0(interleaved)

def reverse_iterative0(s):
    rev_list = empty
    while s != empty:
        rev_list = link(first(s), rev_list)
        s = rest(s)
    return rev_list

def filter_list(predicate, lst):
    """Returns a link only containing elements in lst that satisfy
    predicate.

    >>> lst = link(25, link(5, link(50, link(49, link(80, empty)))))
    >>> new = filter_list(lambda x : x % 2 == 0, lst)
    >>> print_link(new)
    50 80
    """
    if lst == empty:
        return lst
    else:
        if predicate(first(lst)):
            return link(first(lst), filter_list(predicate, rest(lst)))
        else:
            return filter_list(predicate, rest(lst))

def reverse_iterative(s):
    """Return a reversed version of a linked list s.

    >>> primes = link(2, link(3, link(5, link(7, empty))))
    >>> reversed_primes = reverse_iterative(primes)
    >>> print_link(reversed_primes)
    7 5 3 2
    """
    "*** YOUR CODE HERE ***"

def reverse_recursive(s):
    """Return a reversed version of a linked list s.

    >>> primes = link(2, link(3, link(5, link(7, empty))))
    >>> reversed_primes = reverse_recursive(primes)
    >>> print_link(reversed_primes)
    7 5 3 2
    """
    "*** YOUR CODE HERE ***"

def kth_last(lst, k):
    """Return the kth to last element of `lst`.

    >>> lst = link(1, link(2, link(3, link(4))))
    >>> kth_last(lst, 0)
    4
    >>> print(kth_last(lst, 5))
    None
    """
    "*** YOUR CODE HERE ***"
