from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res

    def driver_encode_decode(self):
        input_str = ["neet", "code", "love", "you"]
        output_str = ["neet", "code", "love", "you"]
        print(self.encode(input_str))
        print(type(self.encode(input_str)))
        print(self.decode(self.encode(input_str)))
        if output_str == self.decode(self.encode(input_str)):
            print("PASS")
        else:
            print("FAIL")

def main():
    sol = Solution()
    sol.driver_encode_decode()

if __name__ == "__main__":
    main()