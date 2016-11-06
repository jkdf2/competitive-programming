import fileinput

lines = fileinput.input()
num_trees = int(lines.readline())

tree_locations = []
tree_heights   = []
for line in lines:
    index,height = (int(x) for x in line.split(" "))
    tree_locations.append(index)
    tree_heights.append(height)

# Set up dp array and recall that the first tree can always
# fall left safely.
# dp = [[0 for _ in range(2)] for _ in range(len(tree_locations))]
# dp[0][0] = 1
# if len(tree_locations) == 1 or tree_locations[1]>tree_locations[0]+tree_heights[0]:
    # First tree can safely fall right
#     dp[0][1] = 1
# Else first tree can only fall left.

# Can always cut leftmost tree left and rightmost tree right
cuts = 2 if len(tree_locations) > 1 else len(tree_locations)

for i in range(1,len(tree_locations)-1):
    # try to cut left first
    if tree_locations[i] - tree_heights[i] > tree_locations[i-1]:
        cuts += 1
    elif tree_locations[i] + tree_heights[i] < tree_locations[i+1]:
        cuts += 1

        # 'transplant' the tree as far right as it fell.
        tree_locations[i] += tree_heights[i]

    # otherwise we can't cut any direction :( poor tree
    # or maybe lucky tree :)

print(cuts)
