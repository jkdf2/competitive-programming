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
dp = [[0 for _ in range(2)] for _ in range(len(tree_locations))]
dp[0][0] = 1
if len(tree_locations) == 1 or tree_locations[1]>tree_locations[0]+tree_heights[0]:
    # First tree can safely fall right
    dp[0][1] = 1
# Else first tree can only fall left.

for i in range(1, len(tree_locations)):
    dp[i][1] = max(dp[i-1][0],dp[i-1][1])

    # Can this tree fall right?
    try:
        if tree_locations[i] + tree_heights[i] < tree_locations[i+1]:
            # Yes, I can fall right, so that's one more tree that can fall.
            dp[i][1] += 1
    except IndexError:
        # I can always fall right if I'm the last tree. Yay me!
        dp[i][1] += 1
    # otherwise, I cannot fall right, so this additional tree cannot fall,
    # no change.

    # Can this tree fall left?
    # May depend on if left tree fell right or not!
    if tree_locations[i-1]+tree_heights[i-1]<tree_locations[i]-tree_heights[i]:
#         print("{} can fall left no matter what".format(tree_heights[i]))
        # Doesn't matter how the left tree fell, I'm good to fall left
        dp[i][0] = 1 + max(dp[i-1][0],dp[i-1][1])
    elif tree_locations[i-1]<tree_locations[i]-tree_heights[i]:
#         print("{} can fall left, conditionally".format(tree_heights[i]))
        # I can only fall left if the tree beside me didn't fall right.
        # Find the better between me falling and him not, or vice versa.
        dp[i][0] = max(dp[i-1][1],1+dp[i-1][0])

print(max(dp[len(tree_locations) - 1]))
