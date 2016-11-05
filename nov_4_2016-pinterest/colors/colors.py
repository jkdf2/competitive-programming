import fileinput

lines = fileinput.input()

num_tests = int(lines.readline())
for _ in range(num_tests):
    line = lines.readline().strip().split()
    num_colors = int(line[0])
    this_color = line[1][1:]

    colors = []

    for _ in range(num_colors):
        colors.append(lines.readline().strip()[1:])

    # Sort first by ASCII, then by distance. Python is <3
    colors.sort()
    colors.sort(key=lambda c: (int(this_color[0:2],base=16)-int(c[0:2],base=16))**2 +
                              (int(this_color[2:4],base=16)-int(c[2:4],base=16))**2 +
                              (int(this_color[4:6],base=16)-int(c[4:6],base=16))**2)
    print("Case #{}:".format(this_color))
    for color in colors:
        print("#{}".format(color))
