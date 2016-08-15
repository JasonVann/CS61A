def vending_machine(snacks):
    """Cycles through list of snacks.
    
    >>> vender = vending_machine(['chips', 'chocolate', 'popcorn'])
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(['brownie'])
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    i = 0
    def cycle():
        nonlocal i
        #print(snacks[i])
        snack = snacks[i]
        i += 1
        if i >= len(snacks):
            i = 0
        return snack
    return cycle
