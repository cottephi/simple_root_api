EPSILON = 1e-6

DEBUG = False


def racine(x: float) -> float:
    """ Approximate the root square of a real number

    Parameters
    ----------
    x: float
        The value of which the square root must be computed

    Returns
    -------
    float:
        The approximated square root

    Raises
    ------
    ValueError:
        If x is negative (complex numbers not supported)

    Examples
    -------
    >>> value = 28.
    >>> racine(value)
    5.291502596731155
    >>> value = 0.5
    0.7071066756575051

    Notes
    -----
    The algorithm works by dichotomy : it starts by setting a lower and an upper limit between which the solution must
    be.
    It then tries the value in the middle, and sets the low limit to the tried value if the squared value is lower than
    x, or halves the upper limit if the squared value if greater than expected.
    It stops if the absolute value of the difference between x and the squared value is lower than epsilon=1e-6.
    The initial value for the lower limit is 1, the initial value for the upper limit if x / 2 if x is greater than 4,
    else it is x itself.
    If x if less than 1, the function calls itself with 1/x as argument, and returns the inverse of the result.
    If x is 0, the function immediatly returns 0
    """

    def get_remain():
        return y ** 2 - x

    if x < 0.:
        raise ValueError("Can not compute root square of a negative number")
    if x == 0.:
        return 0.
    if x < 1.:
        return 1. / racine(1. / x)
    if x < 4.:
        high = x
    else:
        high = x / 2.

    low = 1
    y = high / 2.
    remain = get_remain()
    steps = 0

    if DEBUG:
        print("y:", y, "x:", x, "y²:", y ** 2, "high:", high, "low:", low, "remain:", remain, "epsilon:", EPSILON)
        print("")

    while abs(remain) > EPSILON:

        if remain > 0:
            if DEBUG:
                print("Too high: lower limit stays at", low, "while upper limit goes from", high, "to", high / 2.)
            high = y
            y = high / 2.
        else:
            if DEBUG:
                print("Too low: lower limit goes from", low, "to", y, "while upper limit stays at", high)
            low = y
            y = low + (high - low) / 2.
        remain = get_remain()
        if DEBUG:
            print("y:", y, "x:", x, "y²:", y ** 2, "high:", high, "low:", low, "remain:", remain, "epsilon:", EPSILON)
            print("")
            steps += 1
    if DEBUG:
        print("solved in", steps, "steps")
    return y
