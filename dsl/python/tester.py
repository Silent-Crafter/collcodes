from itertools import permutations
from random import randint
from timeit import timeit
# from bubblesort import bubbleSort


class Tester:
    def __init__(self, size, output=False, *args):
        self.size = size
        self.failed = 0
        self.output = output

        self.tot_time = 0

        self.args = args

    def test(self, func):
        l: list[int] = [randint(1, 100) for i in range(self.size)]
        count = 0

        perms = permutations(l)

        for item in list(perms):
            temp = list(item)
            s = temp.copy()
            s.sort()

            time = timeit(lambda: func(temp), number=1)
            count += 1
            self.tot_time += time

            if self.output: print(f'[TESTER] Tested for {item=}  result={temp}  expected={s}')
            if temp != s:
                self.failed += 1
                if self.output:
                    print(f"Test failed for {item}.")

        if not self.failed:
            print(f"[TESTER] Average execution time {self.tot_time/count}")
        else:
            print(f"Tests Passed: {count-self.failed}/{count}")
