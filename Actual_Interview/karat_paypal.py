"""
We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room,
write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit.
(All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter.
(The room is empty when the log begins.)

Each collection should contain no duplicates,
regardless of how many times a given employee matches the criteria for belonging to it.

records1 = [
  ["Paul",     "enter"],
  ["Pauline",  "exit"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Martha",   "exit"],
  ["Joe",      "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Joe",      "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Joe",      "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Joe",      "enter"],
  ["Joe",      "enter"],
  ["Martha",   "exit"],
  ["Joe",      "exit"],
  ["Joe",      "exit"] 
]

Expected output: ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]

Other test cases:

records2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

records3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

records4 = [
  ["Raj", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Raj", "enter"],
]

Expected output: ["Raj", "Paul"], ["Paul"]

All Test Cases:
mismatches(records1) => ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"]
mismatches(records2) => [], []
mismatches(records3) => ["Paul"], ["Paul"]
mismatches(records4) => ["Raj", "Paul"], ["Paul"]

n: length of the badge records array

records1 = [
    ["Paul", "enter"],
    ["Pauline", "exit"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Martha", "exit"],
    ["Joe", "enter"],
    ["Martha", "enter"],
    ["Steve", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Joe", "enter"],
    ["Curtis", "exit"],
    ["Curtis", "enter"],
    ["Joe", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"],
    ["Joe", "enter"],
    ["Joe", "enter"],
    ["Martha", "exit"],
    ["Joe", "exit"],
    ["Joe", "exit"],
]
records2 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
]
records3 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]
records4 = [
    ["Raj", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
    ["Raj", "enter"],
]
"""


def mismatches(records):
    # Track current state of employees (inside or outside)
    state = {}
    # Track employees with mismatches
    invalid_entries = set()
    invalid_exits = set()

    for name, action in records:
        if action == "enter":
            if name in state and state[name] == "inside":
                # Duplicate entry: already inside
                invalid_entries.add(name)
            state[name] = "inside"
            print(name, action, state)
        else:  # action == "exit"
            if name not in state or state[name] == "outside":
                # Exit without entry
                invalid_exits.add(name)
            state[name] = "outside"
            print(name, action, state)

    # Check for employees left inside (no exit)
    print(state)
    for name, status in state.items():
        if status == "inside":
            invalid_entries.add(name)

    # Convert sets to sorted lists
    return list(invalid_entries), list(invalid_exits)


def driver_find_enter_exit():
    """"
    mismatches(records1) => ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline",  "Curtis", "Joe"]
    mismatches(records2) => [], []
    mismatches(records3) => ["Paul"], ["Paul"]
    mismatches(records4) => ["Raj", "Paul"], ["Paul"]
    """

    records1 = [
        ["Paul", "enter"],
        ["Pauline", "exit"],
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Martha", "exit"],
        ["Joe", "enter"],
        ["Martha", "enter"],
        ["Steve", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "enter"],
        ["Joe", "enter"],
        ["Curtis", "exit"],
        ["Curtis", "enter"],
        ["Joe", "exit"],
        ["Martha", "enter"],
        ["Martha", "exit"],
        ["Jennifer", "exit"],
        ["Joe", "enter"],
        ["Joe", "enter"],
        ["Martha", "exit"],
        ["Joe", "exit"],
        ["Joe", "exit"],
    ]

    print(f"records = {records1} ")
    print(f"mismatched =  {mismatches(records1)}")
    print(f"expected = ", ["Steve", "Curtis", "Paul", "Joe"], ["Martha", "Pauline", "Curtis", "Joe"])

    records2 = [
         ["Paul", "enter"],
         ["Paul", "exit"],
     ]
    print(f"records = {records2} ")
    print(f"mismatched =  {mismatches(records2)}")
    print(f"expected = ", [], [])


    records3 = [
        ["Paul", "enter"],
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"],
    ]
    print(f"records = {records3} ")
    print(f"mismatched =  {mismatches(records3)}")
    print(f"expected = ", ['Paul'], ['Paull'])

    # records4 = [
    #     ["Raj", "enter"],
    #     ["Paul", "enter"],
    #     ["Paul", "exit"],
    #     ["Paul", "exit"],
    #     ["Paul", "enter"],
    #     ["Raj", "enter"],
    # ]


def main():
    driver_find_enter_exit()


if __name__ == "__main__":
    main()
