
def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    valleys = 0
    in_valley = False

    L_path = list(path)
    for step in L_path:
        if step == 'U':
            sea_level += 1
        elif step == 'D':
            sea_level -= 1
        #
        # if sea_level < 0 and not in_valley:
        #     valleys += 1
        #     in_valley = True
        # elif sea_level > 0 and in_valley:
        #     in_valley = False

        if sea_level < 0 :
            in_valley = True
        elif sea_level > 0 :
            in_valley = False

        if sea_level == 0 and in_valley:
            valleys += 1
            in_valley = False

    print(valleys)
    return valleys


def main():

    steps = 12
    path = ("DDUUDDUDUUUD")

    countingValleys(steps, path)

    steps = 8
    path = "UDDDUDUU"
    countingValleys(steps, path)

    steps = 12
    path = "DDUUDDUDUUUD"
    countingValleys(steps, path)

    steps = 10
    path = "UDUUUDUDDD"
    countingValleys(steps, path)

    steps = 10
    path = "DDUUUUDDDD"
    countingValleys(steps, path)


if __name__ == "__main__":
    main()