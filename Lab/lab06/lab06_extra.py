## Optional Questions ##

# Shakespeare and Dictionaries
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev].append(word)
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def sent():
    return construct_sent('The', table)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)

# pyTunes Trees
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    return tree(username, 
                [tree('pop', 
                    [tree('justin bieber', 
                        [tree('single', 
                            [tree('what do you mean?')])]), 
                    tree('2015 pop mashup')]), 
                tree('trance', 
                    [tree('darude', 
                        [tree('sandstorm')])])])

def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    #print('a')
    #print_tree(t)
    if is_leaf(t):
        return 1
    else:
        node, tree = entry(t), children(t)
        if len(tree) > 1:
            return num_songs(tree[0]) + num_songs(tree[1])
        else:
            return num_songs(tree[0])

def num_songs2(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    if is_leaf(t):
        return 1
    return sum([num_songs2(b) for b in children(t)])

def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('vance joy',
    ...                       [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    '''
    node, tree = entry(t), children(t)
    #print(node, tree)
    while node != category:
        node = entry(tree)
        tree = children(node)
        node = node[0]
        #print('b', node, tree)
    print('c', tree)
    tree = tree + [song]
    print('d', tree)
    print('e', t)
    '''

    if(entry(t) == category):
        return tree(entry(t), children(t) + [tree(song)])

    kept_children = []
    for b in children(t):
        kept_children += [add_song(b, song, category)]
    #print(kept_children)
    return tree(entry(t), kept_children)

def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    #if entry(t) == target:
    #   return None
    '''
    all = [delete(b, target) for b in children(t) if entry(t) != target]
    print('a', all)
    return tree(entry(t), all)
    '''
    kept_children = []
    for b in children(t):
        if entry(b) != target:
            kept_children += [delete(b, target)]
    return tree(entry(t), kept_children)

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