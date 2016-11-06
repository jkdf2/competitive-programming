import fileinput

lines = fileinput.input()

# discard line 0, we don't need it.
lines[0]

# convert all of line 1 into a list of integers
lst = [int(k) for k in lines[1].split()]

for left_index in range(len(lst)):
    for right_index in range(len(lst) - 1, left_index, -1):
        if (lst[left_index] > lst[right_index]):
            diff = lst[left_index] - lst[right_index]
            lst[right_index] += diff
            lst[left_index] -= diff

print(" ".join(str(e) for e in lst))
