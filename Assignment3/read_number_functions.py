# Basic function named mean to get the average of all the numbers


def mean(lst):
    total = 0
    for nums in lst:
        total += nums
    mean = total // len(lst)
    return mean


# Standard division function for computing the outcome


def standart_devision(lst1, mn):
    lst = []
    ttl = 0
    for numbers in lst1:
        value = (numbers - mn)**2
        lst += [value]
        ttl += value

    stndrt = (1/len(lst1))*ttl
    final = stndrt ** 0.5
    return final