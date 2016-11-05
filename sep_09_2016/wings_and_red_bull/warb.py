import fileinput
from collections import deque

def main():
    lines = fileinput.input()
    test_cases = int(lines.readline().strip())

    best_seen = None
    for _ in range(test_cases):
        test_params = lines.readline().split(" ")
        tgt = int(test_params[0])
        cooling = int(test_params[1])
        num_wings = int(test_params[2])
#         print("tgt: {} | cooling: {} | num_wings: {}".format(tgt, cooling, num_wings))
        wings = list()
        for _ in range(num_wings):
            wings.append(int(lines.readline().strip()))

        # now I have all of the data
        states = deque()
        states.append(State(0,0))

        while len(states) is not 0:
            state = states.popleft()
            print("examining state with heat {} and steps {}".format(state.heat, state.steps))
            if best_seen is None or state.steps < best_seen:
                if state.heat is tgt:
                    if best_seen is None:
                        best_seen = state.steps
                    elif state.steps < best_seen:
                        best_seen = state.steps
                else:
                    if state.heat > tgt and cooling is not 0:
                        states.append(State(state.heat - cooling, state.steps))
                    for heat in wings:
                        states.append(State(state.heat + heat, state.steps + 1))
        print(best_seen)


class State():
    def __init__(self, heat, steps):
        self.heat = heat
        self.steps = steps
    
    def __repr__(self):
        return("State with heat {} and steps {}".format(self.heat, self.steps))

main()
