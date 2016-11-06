import fileinput

def main():
    lines = fileinput.input()
    x = lines.readline().strip()

    moves = 0
    carry = False
    for digit in x[1:][::-1]:
        if digit == "0":
            if not carry:
                moves += 1
            else:
                moves += 2
        else:
            if carry:
                moves += 1
            else:
                carry = True
                moves += 2

    if x[0] == 1 and carry:
        moves += 1

    print(moves)

main()
