import fileinput

lines = fileinput.input()
lines[0]

for line in lines:
    line = line.strip()
    if len(line.split(" ")) is 1:
        print("{} Returns".format(line))
    else:
        print("{}: Age of Darkness".format(line))
