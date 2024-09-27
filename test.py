from collections import defaultdict

input_s = ["act", "pots", "tops", "cat", "stop", "hat"]


def anagram(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for s in strs:
        word = [0] * 26
        for c in s:
            word[ord(c) - ord('a')] += 1

        res[tuple(word)].append(s)

    return res.values()


print(anagram(input_s))