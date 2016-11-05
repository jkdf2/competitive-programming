import fileinput
lines = fileinput.input()

num_tests = int(lines.readline())
for _ in range(num_tests):
    num_nodes = int(lines.readline())

    nodes = dict()
    for _ in range(num_nodes - 1):
        p,c = (int(x) for x in lines.readline().split())

        try:
            n1 = nodes[p]
        except KeyError:
            n1 = set()

        try:
            n2 = nodes[c]
        except KeyError:
            n2 = set()

        n1.add(c)
        n2.add(p)
        nodes[p] = n1
        nodes[c] = n2

    result = []
    while len(nodes) > 2:
        m = num_nodes + 1
        for node, neighbors in nodes.items():
            if len(neighbors) == 1 and node < m:
                m = node
        parent = nodes.pop(m).pop()
        nodes[parent].remove(m)

        result.append(parent)
#         print(nodes)
#         print(result)

    print(result)
