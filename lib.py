class Collatz:
    lengths = {}

    def __init__(self, initial_value):
        self._initial_value = initial_value
        self._current_value = initial_value
        length = 1
        for i in self:
            try:
                length += Collatz.lengths[i]
                break
            except KeyError:
                length += 1
        Collatz.lengths[initial_value] = length
        self._current_value = self._initial_value

    def __next__(self):
        if self._current_value == 1:
            raise StopIteration
        elif self._current_value % 2 == 0:
            self._current_value = self._current_value // 2
        else:
            self._current_value = self._current_value * 3 + 1
        return self._current_value

    def __iter__(self):
        return self


def gen_collatz(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


collatzlengths = {}


def collatz_length(n):
    length = 0
    for j in gen_collatz(n):
        try:
            length += collatzlengths[j]
            break
        except KeyError:
            length += 1
    collatzlengths[n] = length


def eulercoins():
    a = 1504170715041707
    b = 4503599627370517
    cur = a % b
    n = 2
    min_coin = 1504170715041707
    ns = []
    coins = []
    yield min_coin
    while cur > 1:
        if (cur := ((a * n) % b)) < min_coin:
            min_coin = cur
            ns.append(n)
            coins.append(min_coin)
            yield min_coin
        n += 1

    pass


if __name__ == "__main__":
    for i in range(1, 2001):
        collatz_length(i)
    pass
