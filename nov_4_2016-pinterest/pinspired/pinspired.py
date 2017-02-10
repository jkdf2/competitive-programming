import fileinput

non_puns = set(["pin", "pins", "pinned", "pinning", "pinner", "pinners"])

lines = fileinput.input()
num_tests = int(lines.readline())

for _ in range(num_tests):
    puns = 0
    words = lines.readline().strip().lower().split()
    for word in words:
        if word in non_puns:
            # This word is a literal "pin" and not a pun! Skip!
            continue
        if "pin" in word:
            # The word is a pun! Count it :)
            puns += 1

    print(puns)
