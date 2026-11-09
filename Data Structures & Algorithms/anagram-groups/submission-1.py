class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        counts = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                key = ord(char) - ord('a')
                count[key] += 1
            if tuple(count) not in counts:
                counts[tuple(count)] = [word]
            else:
                counts[tuple(count)].append(word)
        for k, v in counts.items():
            res.append(v)
        return res