import fileinput


non_puns = set(["pin", "pins", "pinned", "pinning", "pinner", "pinners"])

lines = fileinput.input()
num_tests = int(lines.readline())

for _ in range(num_tests):
    puns = 0
    words = lines.readline().strip().lower().split()
    for word in words:
        if word in non_puns:
#             print("{} is a non_pun".format(word))
            continue
        if "pin" in word:
#             print("{} is a pun".format(word))
            puns += 1

    print(puns)
