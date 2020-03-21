
class Collatz:
    lengths = {1: 1}

    def __init__(self, initial_value):
        self._initial_value = initial_value
        self._current_value = initial_value
        visits = [self._initial_value]
        length = 1
        for i in self:
            try:
                length += Collatz.lengths[i]
                break
            except KeyError:
                length += 1
                visits.append(i)

        for idx, val in enumerate(visits):
            Collatz.lengths[val] = length - idx

    def __next__(self):
        if self._current_value % 2 == 0:
            self._current_value = self._current_value // 2
        else:
            self._current_value = (self._current_value * 3 + 1)
        return self._current_value

    def __iter__(self):
        return self


if __name__ == '__main__':
    Collatz(10)
    pass
