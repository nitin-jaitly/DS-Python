from collections import defaultdict

def group_analgram(nums: list[str],n) -> list[list[str]]:
    ## Mapping character count to list of Anagrams
    res = defaultdict(list)

    for s in nums:
        count = 0  * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


