def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) + lower_bound(y)
    p4 = upper_bound(x) + upper_bound(y)
    return [min(p1, p2, p3, p4), max(p1, p2, p3, p4)]

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    assert lower_bound(y) * upper_bound(y) > 0, 'The dividend shouldn\'t span over 0'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(1, 3) # Replace this line!
    r2 = interval(2, 4) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    # Sol from CS61A
    return """The multiple reference problem exists.  The true value
    within a particular interval is fixed (though unknown).  Nested
    combinations that refer to the same interval twice may assume two different
    true values for the same interval, which is an error that results in
    intervals that are larger than they should be.

    Consider the case of i * i, where i is an interval from -1 to 1.  No value
    within this interval, when squared, will give a negative result.  However,
    our mul_interval function will allow us to choose 1 from the first
    reference to i and -1 from the second, giving an erroneous lower bound of
    -1.

    Hence, a program like par2 is better than par1 because it never combines
    the same interval more than once.
    """

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    p0 = a*lower_bound(x)**2 + b*lower_bound(x) + c
    p1 = a*upper_bound(x)**2 + b*upper_bound(x) + c
    m = - b/(2*a)
    if m > upper_bound(x) or m < lower_bound(x):
        #print('a', p0, p1, m)
        return interval(min(p0, p1), max(p0, p1))
    else:
        pm = a*m**2 + b*m + c
        #print('b', p0, p1, m, pm)
        return interval(min(p0, pm, p1), max(p0, pm, p1))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    def add_fn(coeff, k, f):
        return lambda x: coeff * pow(x, k) + f(x)

    def add_dfn(coeff, k, df):
        return lambda x: k * coeff * pow(x, k-1) + df(x)

    def add_ddfn(coeff, k, ddf):
        return lambda x: k * (k-1) * coeff * pow(x, k-2) + ddf(x)

    # Define the polynomial and its first and second derivatives.
    f = lambda x: 0
    df = lambda x: 0
    ddf = lambda x: 0
    for k, coeff in enumerate(c):
        f = add_fn(coeff, k, f)
        if k > 0:
            df = add_dfn(coeff, k, df)
        if k > 1:
            ddf = add_ddfn(coeff, k, ddf)

    # Find as many extreme points as we can using Newton's method
    lower, upper = lower_bound(x), upper_bound(x)
    num_steps = 20
    step = (upper - lower) / num_steps
    starts = [lower + k * step for k in range(num_steps)]
    extremums = [find_zero(df, ddf, n) for n in starts]

    # Filter for the interval x and return
    ns = [n for n in extremums if n > lower and n < upper] + [lower, upper]
    values = [f(n) for n in ns]
    #print(values)
    return interval(min(values), max(values))

# Newton's method from lecture

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true or
    max_updates have been applied."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, guess=1):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

def newton_update(f, df):
    """Return an update function for f with derivative df,
    using Newton's method."""
    def update(x):
        return x - f(x) / df(x)
    return update
