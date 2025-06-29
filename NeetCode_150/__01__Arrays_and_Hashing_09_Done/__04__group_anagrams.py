from collections import defaultdict
from typing import List

class Solution:
    def group_analgrams(self, strs: List[str], n) -> List[List[str]]:
        ## Mapping character count to list of Anagrams
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        print(f"res = {res}")
        print(f"res keys = {res.keys()}")
        print(f"res values = {res.values()}")
        return res.values()


    def driver_anagrams(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        print(self.group_analgrams(strs, len(strs)))
        # strs = [""]
        # print(group_analgrams(strs, len(strs)))
        #
        # strs = ["a"]
        # print(group_analgrams(strs, len(strs)))
        #

def main():
    sol = Solution()
    print(sol.driver_anagrams())

if __name__ == "__main__":
    main()