 Turns the list to set and gives the amount of unique numbers
def count_differences(intgrs):
    numset = set(intgrs)
    for i in intgrs:
        numset.add(i)
    return len(set(numset))


# Adds each number to the dictionary with value
# (corresponding occurencies) and stores them
def count_occurencies(intgrs):
    empty = {}
    for keys in intgrs:
        if keys not in empty:
            empty[keys] = 0
        empty[keys] += 1
    return empty
