class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
        
        count2 = {}
        for j in range(len(t)):
            if t[j] not in count2:
                count2[t[j]] = 1
            else:
                count2[t[j]] += 1

        return count == count2
        