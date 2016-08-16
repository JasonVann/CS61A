# Extra Questions


class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        if index == 0:
            self.first = element
        elif self.rest is Link.empty:
            raise IndexError
        else:
            self.rest[index - 1] = element

    def __contains__(self, e):
        return self.first == e or e in self.rest

    def map(self, f):
        self.first = f(self.first)
        if self.rest is not Link.empty:
            self.rest.map(f)

# Q4
    def __add__(self, other):
        """Adds two Links, returning a new Link

        >>> Link(1, Link(2)) + Link(3, Link(4, Link(5)))
        Link(1, Link(2, Link(3, Link(4, Link(5)))))
        """
        b = self.rest
        res = Link.empty
        while self != Link.empty:
            res = Link(self.first, res)
            self = self.rest

        #other = Link.empty
        while other != Link.empty:
            res = Link(other.first, res)
            other = other.rest

        #print_link(res)
        res = reversed(res)
        #res.rest = other
        return res


# Q5
    def __reversed__(self):
        """Return a reversed version of the Link.

        >>> reversed(Link(1, Link(2, Link(3))))
        Link(3, Link(2, Link(1)))
        """
        a = self
        first, rest = a.first, a.rest
        res = Link.empty
        while a.rest != Link.empty:
            res = Link(first, res)
            a = a.rest
            first, rest = a.first, a.rest
        res = Link(a.first, res)
        return res
# Q6
    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1, 2, 3, 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        if self == Link.empty:
            return '()'

        res = '<'
        while self != Link.empty:
            res += str(self.first) + ', '
            self = self.rest
        res = res[:-2]
        res += '>'
        return res

        '''OR
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ', '
            self = self.rest
        return string + str(self.first) + '>'
        '''

# Q8
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        self.current += 1
        return self.current - 1

    def __iter__(self):
        return IteratorRestart(self.start, self.end)

# Q9
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    def __init__(self, s):
        self.s = s
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        #print('current', self.current)
        if self.current >= len(self.s):
            raise StopIteration

        self.current += 1
        return self.s[self.current - 1]

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)
