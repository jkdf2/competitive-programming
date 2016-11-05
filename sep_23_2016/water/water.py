import fileinput
from collections import deque

def main():
    lines = fileinput.input()
    test_cases = int(lines.readline().strip())

    for _ in range(test_cases):
        num_friends = int(lines.readline().strip())
        invalid = 0
        for _ in range(num_friends):
            line = lines.readline().split(" ")
            H = int(line[0])
            W = int(line[1])
            if not 6 <= H <= 21:
                invalid += 1
            elif not 0 <= W <= 1024:
                invalid += 1

        print(invalid)

main()
