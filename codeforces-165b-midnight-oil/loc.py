import fileinput

def main():
    line = fileinput.input().readline().split(" ")
    n = int(line[0])
    k = int(line[1])

    # Maintain that lo will never be the right amount of code and hi will
    # ALWAYS be enough code to write.
    lo = 0
    hi = n
    while hi - lo > 1:
#         print("lo: {} | hi: {}".format(lo, hi))
        mid = (lo + hi) // 2
        if is_enough(mid, n, k):
#             print("mid {} was enough | setting hi".format(mid))
            hi = mid
        else:
#             print("mid {} was not enough | setting low".format(mid))
            lo = mid

    print(hi)

def is_enough(v, target, k):
    """
    Increase the powers of k until k^p >= v or tally exceeds target.
    """
    k_pow = 1
    tally = 0
    for _ in range(v):
        factor = v // k_pow
        tally += factor
#         print("{} // {} = {} added to tally | tally: {}".format(v, k_pow, factor, tally))
        if tally >= target:
#             print("Tally: {} is greater than target {}".format(tally, target))
            return True
        elif factor == 0:
            return False
        k_pow *= k

main()
