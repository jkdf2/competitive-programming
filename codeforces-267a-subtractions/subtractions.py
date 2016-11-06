import fileinput

lines = fileinput.input()
num_tests = int(lines.readline())

for _ in range(num_tests):
    x,y = lines.readline().split(" ")
    x,y = int(x),int(y)
    x,y = min(x,y),max(x,y)

    ops = 0
    while x > 0:
#         assert(0 < x <= y)
#         print("{} operations turns pair {},{} into {},{}".format(y//x,x,y,x,y%x))
        ops += (y // x)
        x,y = y % x,x
#         x,y = min(x,y),max(x,y)
    print("{}".format(ops))
