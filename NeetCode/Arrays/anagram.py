class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #
        # # ## O(1)
        # return sorted(s) == sorted(t)

        # #O ( n ) solution
        if len(s) != len(t):
            return False
        count_for_S, count_for_T = {} , {}

        for i in range(len(s)):
            count_for_S[s[i]] = 1 + count_for_S.get(s[i], 0)
            count_for_T[t[i]] = 1 + count_for_T.get(t[i], 0)


        for key in count_for_S:
            if count_for_S[key] != count_for_T.get(key, 0):
                return False
        return True


def driver_is_anagram():
    s = ""
