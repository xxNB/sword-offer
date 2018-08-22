import random


# fisher-yates shuffle


def shuffle(lis):
    result = []
    while lis:
        p = random.randrange(0, len(lis))
        result.append(lis[p])
        lis.pop(p)
    return result


# knuth-durstenfeld shuffle

def shuffle1(lis):
    for i in range(len(lis) - 1, 0, -1):
        p = random.randrange(0, i + 1)

        lis[i], lis[p] = lis[p], lis[i]
    return lis


# Inside-Out Algorithm

def shuffle2(lis):
    result = lis[:]
    for i in range(1, len(lis)):
        j = random.randrange(0, i)
        result[i] = result[j]
        result[j] = lis[i]
    return result


r = shuffle([1, 2, 2, 3, 3, 4, 5, 10])
print(r)
