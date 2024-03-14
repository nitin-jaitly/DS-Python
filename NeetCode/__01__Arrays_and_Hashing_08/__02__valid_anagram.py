class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #
        # # ## O(1)
        # return sorted(s) == sorted(t)

        # #O ( n ) solution
        # Check if the anagram candidates are of the same length
        if len(s) != len(t):
            print("String s = " + "\"" + s + "\"" + " is NOT anagram of string t = " + "\"" + t + "\"")
            return False

        count_for_S, count_for_T = {} , {}

        for i in range(len(s)):
            count_for_S[s[i]] = 1 + count_for_S.get(s[i], 0)
            count_for_T[t[i]] = 1 + count_for_T.get(t[i], 0)

        print("S =")
        print(s)
        print(count_for_S)

        print("t =")
        print(t)
        print(count_for_T)

        for key in count_for_S:
            if count_for_S[key] != count_for_T.get(key, 0):
                print("String s = " + "\"" + s + "\"" + " is NOT anagram of string t = " + "\"" + t + "\"")
                return False

        print("String s = " + "\"" + s + "\"" + " is anagram of string t = " + "\"" + t + "\"")
        return True


    def driver_is_anagram(self):
        s = "anagram"
        t = "nagaram"

        self.isAnagram(s, t)

        s = "car"
        t = "rat"

        self.isAnagram(s, t)
