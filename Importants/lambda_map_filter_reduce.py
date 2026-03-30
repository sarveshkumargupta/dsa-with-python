

ann_func = lambda a: a * 2


print(ann_func(4))


print(list(map(ann_func, [2, 3, 4, 5, 6])))


def remove_odd(n):
    return True if n % 2 == 0 else False


print(list(filter(remove_odd, [3, 2, 1, 55, 9, 12, 8])))



from functools import reduce


def mul(a, b): return a * b


print(reduce(mul, [12, 3, 4, 5]))


print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
