import fileinput

x = fileinput.input().readline().strip()
i = len(x) - 1
op = 0
c = 0
while i > 0:
    print("x[i] is: ".format(x[i]))
    if x[i] == '1':
        if c == 0:
            c = 1
            op += 2
        else:
            op += 1
    else:
        if c == 0:
            op += 1
        else:
            op += 2
    i -= 1
if x[i] == '1' and c == 1:
    op += 1
print(op)
