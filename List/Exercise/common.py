# Takes two lists and returns True if they have at least one common member
def commonitems(l1, l2):
    result = False
    for x in l1:
        for y in l2:
            if x == y:
                result = True
                return result


print('Common ele are:', commonitems([1, 2, 3], [3, 4, 5]))
