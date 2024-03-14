

def max_area(height: list[int]) -> int:
    #  Brute Force method
    # res = 0
    # for l in range(len(height)):
    #     for r in range(l+1, len(height)):
    #         area = ( l - r ) * min(height[l], height[r])
    #         res = max(res, area)
    #
    # return res

    # Order of N
    res = 0
    l, r = 0 , len(height) - 1
    while l < r:
        area = ( l - r ) * min(height[l], height[r])
        res = max(res,area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res


