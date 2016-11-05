import fileinput
lines = fileinput.input()

num_tests = int(lines.readline())
for _ in range(num_tests):
    revenue  = 0
    expenses = 0
    num_pins,num_packages,num_orders = (int(x) for x in lines.readline().split())

    pins = dict()
    for _ in range(num_pins):
        line = lines.readline().split()
        
                    # supplies, price of pin
        pin_data = (lines.readline().strip().split(),int(line[1]))

        pins[line[0]] = pin_data

    supplies = dict()
    for _ in range(num_packages):
        line = lines.readline().split()

                      # qty, price of one order
        supply_data = (int(line[1]),int(line[2]))

        supplies[line[0]] = supply_data

    supplies_on_hand = dict()
    for _ in range(num_orders):
        order = lines.readline().split()
        pin   = order[0]
        qty   = int(order[1])

        # Cash in money
        revenue += pins[pin][1] * qty

        # Build this order.
        for _ in range(qty):
            for supply in pins[pin][0]:
                if supply in supplies_on_hand and supplies_on_hand[supply] > 0:
                    # use this "free" supply
                    supplies_on_hand[supply] -= 1
                else:
                    # need to buy an order of this supply
                    expenses += supplies[supply][1]
                    supplies_on_hand[supply] = supplies[supply][0] - 1
                    
    print(revenue - expenses)
