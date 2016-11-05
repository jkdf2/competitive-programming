import fileinput
import heapq

def main():
    lines = fileinput.input()
    test_cases = int(lines.readline().strip())

    for _ in range(test_cases):
        line = lines.readline().split(" ")
        num_bars = int(line[0])
        max_weight = int(line[1])
        l = list()
        for _ in range(num_bars):
            line = lines.readline().split(" ")
            b = Bar(int(line[0]),int(line[1]),int(line[2]))
            heapq.heappush(l,b)

        stolen_weight = 0
        stolen_value  = 0
        while len(l) > 0:
            if stolen_weight == max_weight:
                break

            bar = heapq.heappop(l)
#             print(bar)
            while bar.num > 0 and stolen_weight + bar.weight <= max_weight:
                bar.num -= 1
                stolen_weight += bar.weight
                stolen_value  += bar.value*bar.weight

        print(int(stolen_value))

class Bar():
    def __init__(self,num,weight,value):
        self.num = num
        self.weight = weight
        while self.weight > 1:
            self.num *= 2
            self.weight -= 1
        self.value = value
    def __eq__(self,other):
        return self.value == other.value
    def __lt__(self,other):
        return self.value>other.value
    def __repr__(self):
        return "{} bars with val {} per lb and weight {}".format(self.num,self.value,
                self.weight)
#     def __hash__(self):
#         return self.value+self.weight
main()
