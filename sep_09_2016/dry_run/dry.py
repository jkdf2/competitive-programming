import fileinput

lines = fileinput.input()
lines[0]
for line in lines:
    print("I like {}.".format(line.strip()))
