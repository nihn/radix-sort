from functools import reduce


class ZeroList(list):
    """
    List which returns 0 when requested index is outside it.
    """
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return 0


def counting_sort(array, key=lambda x: x):
    length = key(max(array, key=key))

    counting_array = [list() for _ in range(length + 1)]

    for item in array:
        counting_array[key(item)].append(item)

    return [item for subarray in counting_array for item in subarray]


def convert(number, base):
    new = []
    while number > 0:
        new.append(number % base)
        number //= base
    return ZeroList(reversed(new))


def radix_sort(array, return_base10=True):
    base = len(array)
    helper_array = []
    max_len = 0

    for number in array:
        converted = convert(number, base)
        helper_array.append(converted)
        max_len = max(max_len, len(converted))

    for i in range(max_len):
        helper_array = counting_sort(helper_array, key=lambda x: x[-i-1])

    return [reduce(lambda x, y: x + y[1] * (base ** y[0]),
                   zip(range(len(number)), reversed(number)),
                   0)
            for number in helper_array] if return_base10 else helper_array

