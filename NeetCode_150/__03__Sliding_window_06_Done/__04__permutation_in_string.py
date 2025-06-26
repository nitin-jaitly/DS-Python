"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""
class Solution:
    def check_Inclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0 * 26], [0 * 26]

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = s2[r] - ord['a']
            s2Count[index] += 1
            if s1Count[index] == s2[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = s1[r] - ord['a']
            s2Count[index] -= 1
            if s1Count[index] == s2[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1

        return matches == 26

    def check_Inclusion_2(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count_s1, count_s2 = {}, {}

        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)

        l , r = 0, 1
        while r < len(s2):

            count_s2 = {}
            for i in range(l, r + 1):
                count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)

            if count_s1 == count_s2:
                print("\ns1 matches s2 \n" + "s1 = " + s1 + " \t\tcount_s1 = " + str(count_s1) + "\ns2 = " + s2 + " \tcount_s2 = " + str(count_s2))
                return True

            l += 1
            r += 1

        print("\ns1 and s2 did not match")
        print("s1 =")
        print(s1)
        print(count_s1)

        print("s2 =")
        print(s2)
        print(count_s2)

        return False

    def driver_check_Inclusion(self):
        """
        Example 1:

        Input: s1 = "ab", s2 = "eidbaooo"
        Output: true
        Explanation: s2 contains one permutation of s1 ("ba").
        Example 2:

        Input: s1 = "ab", s2 = "eidboaoo"
        Output: false
        """
        # s1, s2 = "ab", "eidbaooo"
        # assert True == self.check_Inclusion(s1, s2)
        #
        # s1, s2 = "ab", "eidboaoo"
        # assert False == self.check_Inclusion(s1, s2)

        s1, s2 = "ab", "eidbaooo"
        assert True == self.check_Inclusion_2(s1, s2)

        s1, s2  = "ab", "eidboaoo"
        assert False == self.check_Inclusion_2(s1, s2)