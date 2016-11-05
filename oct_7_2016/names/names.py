import fileinput

def main():
    lines = fileinput.input()
    test_cases = int(lines.readline().strip())

    for _ in range(test_cases):
        names = set()
        good = True
        for _ in range(5):
            name = lines.readline().split(" ")[0]
            if name in names:
                print("DISAPPOINTMENT")
                good = False
                break
            else:
                names.add(name)
        if good:
            print("HAPPINESS")
main()
