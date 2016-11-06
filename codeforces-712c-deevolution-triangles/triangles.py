import fileinput

def main():
    lines = fileinput.input()
    line = lines.readline().split(" ")
    old_length = int(line[0])
    new_length = int(line[1])
    edges = [new_length for _ in range(3)]

    seconds = 0
    while edges[0] < old_length:
#         print("Edges before update: {}".format(edges))

        edges[0] = min(old_length, edges[1] + edges[2] - 1)
        seconds += 1
#         print("Edges after update: {} | seconds: {}".format(edges,seconds))
        edges.sort()
    print(seconds)

main()
