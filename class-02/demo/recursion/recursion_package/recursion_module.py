def factorial(n):
    """
    return n! (as it's sometimes written)
    e.g. factorial(3) = 3 * 2 * 1 = 6

    Note: Normally wouldn't name a package or module this way
    but wanted to be really clear about which was which

    Bonus: hover your mouse over the function name when importing
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def reverse_list(lst):
    """recursively reverse a list in place

    Args:
        lst: list
    """

    # often recursive solutions use inner "helper" functions
    def _reverse(left, right):

        # base case, the point at which recursion should stop
        if left >= right:
            return

        # multiple assignment, no need for temp variables
        lst[left], lst[right] = lst[right], lst[left]

        # base case not met above so recursively call
        # to get a little closer to solution
        _reverse(left + 1, right - 1)

    # kick off the helper function
    _reverse(0, len(lst) - 1)

    return lst
