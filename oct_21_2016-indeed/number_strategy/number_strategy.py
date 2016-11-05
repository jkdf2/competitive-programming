import fileinput
import math
from collections import Counter

lines = fileinput.input()
num_tests = int(lines.readline())
for _ in range(num_tests):
    n = int(lines.readline())
    factors = Counter()
    while n % 2 == 0 and n > 1:
        n //= 2
        factors[2] += 1

    for i in range(3, math.ceil(math.sqrt(n)) + 25, 2):
        if n == 1:
            break
        while n % i == 0 and n > 1:
            n //= i
            factors[i] += 1

    if n > 2:
        factors[n] += 1

    ending = sum(v for v in factors.values()) - 1
    ending = max(0,ending)
    winner = "Bob" if ending % 2 == 0 else "Alice"
    print("{} wins after move {}".format(winner,ending))
