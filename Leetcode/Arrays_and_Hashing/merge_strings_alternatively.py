
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""

def mergeAlternately(word1: str, word2: str) -> str:
    res = ""
    for i in range(min(len(word1), len(word2))):
        res += word1[i]
        res += word2[i]

    if len(word1) > len(word2):
        res += word1[i+1:]
    else:
        res += word2[i+1:]

    return res


def driver_mergeAlternatively():
    print("Test 1")
    word1 = "abcd"
    word2 = "pq"
    print(mergeAlternately(word1, word2))

    print("\nTest 2")
    word1 = "ab"
    word2 = "pqrs"
    print(mergeAlternately(word1, word2))

    print("\nTest 3")
    word1 = "abcd"
    word2 = "pq"
    print(mergeAlternately(word1, word2))



