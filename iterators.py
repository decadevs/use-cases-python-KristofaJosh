# Document at least 3 use cases of iterators


def loop_illustration(iterable):
    iter_obj = iter(iterable)
    while True:
        try:
            element = next(iter_obj)
            print(element)
        except StopIteration:
            break


# loop_illustration([1, 2, 3, 4, 5]

# using the inter object
obj = iter([5, 4, 3, 2, 1])

# print(next(obj))
# print(next(obj))
# print(next(obj))


class range_illustration:
    def __init__(self, start=1, max=0):
        self.max = max
        self.start = start

    def __iter__(self):
        self.number = self.start
        return self

    def __next__(self):
        if self.max == self.number:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return number


numbers = range_illustration(5, 10)
for i in numbers:
    print(i)
