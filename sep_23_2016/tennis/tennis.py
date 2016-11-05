import fileinput

def main():
    lines = fileinput.input()
    test_cases = int(lines.readline().strip())
    scores = ["love", 15, 30, 40]

    for _ in range(test_cases):
        line = lines.readline().strip().split(" ")
        num_rallies = int(line[0])
        p1_name = line[1]
        p2_name = line[2]

        # Both players start off at scores[0]
        p1 = {p1_name: 0}
        p2 = {p2_name: 0}
        for rally in range(num_rallies):
            winner = lines.readline().strip()
            if rally == num_rallies - 1:
                break
            if winner in p1:
                p1[winner] += 1
            elif winner in p2:
                p2[winner] += 1
            else:
                print(p2_name)
                print(winner)
                assert(False)

            p1_score_idx = p1[p1_name]
            p2_score_idx = p2[p2_name]
            try:
                if p1_score_idx == p2_score_idx:
                    # Determine if all or deuce
                    if scores[p1_score_idx] < 40:
                        print("{} all".format(scores[p1_score_idx]))
                    elif scores[p1_score_idx] == 40:
                        print("deuce")
                elif p1_score_idx > p2_score_idx:
                    # Determine if printing score or advantage
                    try:
                        print("{} {}".format(scores[p1_score_idx], scores[p2_score_idx]))
                    except IndexError:
                        print("advantage {}".format(p1_name))
                else:
                    # Determine if printing score or advantage
                    assert(p1_score_idx < p2_score_idx)
                    try:
                        print("{} {}".format(scores[p1_score_idx], scores[p2_score_idx]))
                    except IndexError:
                        print("advantage {}".format(p2_name))
            except IndexError: # Index out of bounds means that we still have a deuce
                print("deuce")

        winner = p1_name if p1[p1_name] > p2[p2_name] else p2_name
        print("{} won!".format(winner))

main()
