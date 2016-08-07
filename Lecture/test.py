y = "y"
h = y
def y(y):
    h = "h"
    #print y, 'y'
    if y == h:
        return y + "i"
    #print 'a'
    y = lambda y: y(h)
    return lambda h: y(h)
#y = y(y)(y)

def right_binarize(tree):
    #print 'a', tree
    #if is_leaf(tree):
    if isinstance(tree, int):
        return tree
    if len(tree) > 2:
        #print 'b', tree
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(20)
wd(5)
wd(3)

class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder


