

def collatzlength(n):
    obj = Collatz(n)
    ret = 1
    for i in obj:
        try:
            ret += Collatz.lengths[i]
            break
        except KeyError:
            ret += 1
    Collatz.lengths[n] = ret
    return ret


class Collatz:
    lengths = {1: 1}

    def __init__(self, initial_value):
        self.initial_value = initial_value
        self.current_value = initial_value

    def __next__(self):
        if self.current_value % 2 == 0:
            self.current_value /= 2
        else:
            self.current_value = self.current_value * 3 + 1
        return self.current_value

    def __iter__(self):
        return self


if __name__ == '__main__':
    print(collatzlength(10))
    pass
