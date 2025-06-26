
"""
You are given a string s and an integer k.
 You can choose any character of the string and change it to any other uppercase English character.
 You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
 you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2 "AAABBABA" k = 3
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.


"""

class Solution:

    def char_replacement(self, s:str , k: int) -> int:
        freq = {}
        max_length = 0
        left,right = 0,0
        res = 0

        for right in range(len(s)):
            #Update Frequency of Current char
            freq[s[right]] = 1 + freq.get(s[right], 0)

            # Window size minus most frequqnt char gives replacements needed
            window_size = right - left + 1
            max_freq = max(freq.values())

            replacements = window_size - max_freq

            if replacements > k:
                freq[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    def find_max_count_of_char_in_str(self, string):
        my_hash = {}
        for ch in string:
            my_hash[ch] = 1

        print(f"MY HASH = {my_hash}")
        for ch in string:
            if ch in my_hash.keys():
                my_hash[ch] = my_hash.get(ch, 0) + 1

        print("string = " + string)
        print("char = " + ch)
        print("my_hash = " + str(my_hash))

    def driver_check_max_count(self):
        string = "AABBAAAA"
        self.find_max_count_of_char_in_str(string)


    def driver_longest_repeating_char_replacement(self):
        s = "ABAB"
        k = 2
        assert 4 ==  self.char_replacement(s,k)

        s = "AABABBA"
        k = 1
        assert 4 == self.char_replacement(s,k)

def main():
    sol = Solution()
    sol.driver_check_max_count()
    sol.driver_longest_repeating_char_replacement()


if __name__ == "__main__":
    main()