import random

for i in range(100000):
    edge_a = i
    edge_b = i + 1
    cost = (random.randrange(1, 1000000))
    print("{} {} {}".format(edge_a, edge_b, cost))
