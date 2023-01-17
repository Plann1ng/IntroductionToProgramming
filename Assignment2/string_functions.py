def concat(s, n):
    times = s * n
    return times


def counter(s, x):
    times = s.count(x)
    return times


def reverse(s):
    s = s[::-1]
    return s


def firstlast(s):
    f = s[0]
    g = s[-1]
    return f, g


def two_x(s):
    x = s.count("X")
    if x == 2:
        x = True
    else:
        x = False
    return x


def has_duplicates(s):
    s = s.lower()
    if len(s) == len(set(s)):
        s = False
    else:
        len(s) != len(set(s))
        s = True
    return s
