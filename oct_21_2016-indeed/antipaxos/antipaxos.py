import fileinput

lines = fileinput.input()
num_tests = int(lines.readline())

for _ in range(num_tests):
    smallest = int(lines.readline())
    legislators = dict()
    for _ in range(smallest):
        line = lines.readline().strip().split(" ")
        neighbors = set()
        for neighbor in line[1:]:
            neighbors.add(neighbor)

        # Kidnap the motherfucker who doesn't know anyone
        if len(neighbors) == 0:
            smallest = 0
            break

        legislators[line[0]] = neighbors

    if smallest == 0:
        print(1)
        continue

    # Go through all the neighbors' neighbors' ... neighbors' neighbors'
    for legislator,_n in legislators.items():
        gaggle = set(legislator)

        neighbors = list(_n)

        while neighbors:
            n = neighbors.pop()
            if n not in gaggle:
                gaggle.add(n)
                for x in legislators[n]:
                    neighbors.append(x)
            
        if len(gaggle) < smallest:
            smallest = len(gaggle)

    print(smallest)
