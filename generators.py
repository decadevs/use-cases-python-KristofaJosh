# Document at least 3 use cases of generators


def counter(number):
    for x in range(1, number + 1):
        yield x


class Stack_illustration:
    def __init__(self, li):
        self.li = li

    def add_to_stack(self, val):
        self.li.append(val)

    def del_from_stack(self):
        self.li.pop()

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        if self.max == len(self.li):
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return number


s = Stack_illustration([1, 2, 3, 4, 5, 6])

print(s)
