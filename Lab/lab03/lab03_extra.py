from lab03 import *

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def count_up1(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    i = 1
    if i == n:
        return
    print(i)
    i += 1
    count_up1(n-1)

def count_up2(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    i = 1
    if i > n:
        return
    print(i)
    i += 1
    count_up2(n - 1)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i <= n:
            print(i)
            counter(i+1)
    counter(1)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    if a > b:
        return gcd(b, a % b)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    if b > 0:
        return a + ab_plus_c(a, b-1, c)
    else:
        return c

def has_sublist0(l, sublist):
    """Returns whether the elements of sublist appear in order anywhere within list l.
    >>> has_sublist([], [])
    True
    >>> has_sublist([3, 3, 2, 1], [])
    True
    >>> has_sublist([], [3, 3, 2, 1])
    False
    >>> has_sublist([3, 3, 2, 1], [3, 2, 1])
    True
    >>> has_sublist([3, 2, 1], [3, 2, 1])
    True
    """
    sublist_length = len(sublist)
    l_length = len(l)
    if sublist_length > l_length:
        return False
    i = 0
    j = 0
    if sublist_length == 0:
        return True

    while i < l_length:
        
        while j < sublist_length:
            if l[i] == sublist[j]:
                j += 1
                i += 1
            else:
                if j > 0:
                    j = 0
                else:
                    i += 1

            if j == sublist_length - 1:
                return True
            if i == l_length - 1:
                return False

    return False

def has_sublist(l, sublist):
    """Returns whether the elements of sublist appear in order anywhere within list l.
    >>> has_sublist([], [])
    True
    >>> has_sublist([3, 3, 2, 1], [])
    True
    >>> has_sublist([], [3, 3, 2, 1])
    False
    >>> has_sublist([3, 3, 2, 1], [3, 2, 1])
    True
    >>> has_sublist([3, 2, 1], [3, 2, 1])
    True
    """
    sublist_length = len(sublist)
    l_length = len(l)
    if sublist_length > l_length:
        return False
    elif l[0: sublist_length] == sublist:
        return True
    else:
        return has_sublist(l[1:], sublist)

def remove_first(lst, elem):
    """ This function removes the first appearance of elem in list lst.

    >>> remove_first([3, 4] , 3)
    [4]
    >>> remove_first([3, 4, 3] , 3)
    [4, 3]
    >>> remove_first([2, 4] , 3)
    [2, 4]
    >>> remove_first([] , 0)
    []
    """
    if len(lst) == 0:
        return []
    elif elem == lst[0]:
        return lst[1:]
    else:
        return lst[:1] + remove_first(lst[1:], elem)

def sort(lst):
    """This function returns a sorted version of the list lst.

    >>> sort([6, 2, 5])
    [2, 5, 6]
    >>> sort([2, 3])
    [2, 3]
    >>> sort([3])
    [3]
    >>> sort([])
    []
    """ 
    if len(lst) > 0:
        a = min(lst)
        temp = remove_first(lst, a)
        blank = []
        return [a] + sort(temp)
    else:
        return []

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    def func(i, f1, f2):
        if i < n:
            return f1(i) + func(i+1, f2, f1)
        else:
            return f1(i)
    return func(1, odd_term, even_term)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    lst = [int(i) for i in str(n)]
    i = 0
    count = 0
    j = 0
    while i < len(lst) - 1:
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == 10:
                #print lst[i], lst[j]
                count += 1
            j += 1
        i += 1

    return count

    '''
    while True:
        first = lst[0]
        comple = 10 - lst[0]
        if comple in lst:
            lst.remove(first)
            lst.remove(comple)
            count += 1
        else:
            i += 1
        if i > len(lst) - 1:
            break
    return count

    lst = []
    while n > 0:
        lst.append(n%10)
        n = n // 10

    def count(i, lst):
        pass
    print lst
    '''

ten_pairs(7823952)

def ten_pairs2(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs2(n//10) + count_digit(n//10, 10 - n%10)

def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    """
    if n == 0:
        return 0
    else:
        if n%10 == digit:
            return count_digit(n//10, digit) + 1
        else:
            return count_digit(n//10, digit)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def incre(i):
        if i ** 2 > n:
            return True
        elif n % i == 0:
            return False
        else:
            return incre(i+1)
    if n <= 2:
        return True
    else:
        print incre(2)

def is_prime2(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    import math
    def helper(i):
        if i < math.sqrt(n): #could replace with i == 1
            return True
        if n % i == 0:
            return False
        return helper(i - 1)
    return helper(n - 1)