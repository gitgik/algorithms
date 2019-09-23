def fibonacci(n, memoize={1:0, 2: 1}):
    # check for integers
    if type(n) != int:
        raise TypeError('Value of n must be an integer')
    if n < 0:
        raise TypeError('Value of n must be a positive integer')
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fibonacci(n - 1, memoize) + fibonacci(n - 2, memoize)
        return memoize[n]
