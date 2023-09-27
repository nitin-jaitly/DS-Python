from heapq import heappush


def maximum_capital(c, k, capitals, profits):
    current_capital = 2
    profits_max_heap = []

    print("\tIdentifying projects we can afford with our"
          " current capital of {current_capital}:")
    # Select projects (in the range of the current capital)
    # then push them onto the max-heap

    # As, heapq is a min heap, but we need a max heap
    # so we will store negated elements
    for i in range(len(profits)):
        if capitals and capitals[i] <= current_capital:
            heappush(profits_max_heap, (-profits[i]))
            print("\t\tProfit of project (with capital requirement of ",
                  current_capital, "pushed on to max-heap = ", profits[i])

    return profits_max_heap



def print_capitals_min_heap(capitals):
    arr = []
    for i in range(len(capitals)):
        arr.append(capitals[i])
        print("\t", arr)


def driver_maximize_capital():
    input = (
            (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
            (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
            (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
            (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
            (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
            )
    num = 1
    for i in input:
        print(f"{num}.\tGiven Capitals: {i[2]}")
        print("\tAdding capital values...")
        capital = maximum_capital(i[0], i[1], i[2], i[3])
        print_capitals_min_heap(capital)
        print("-" * 100, "\n")
        num += 1

