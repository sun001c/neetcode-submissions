class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            count = [0] * 26
            for j in range(len(strs[i])):
                ord_key = ord(strs[i][j]) - ord('a')
                count[ord_key] += 1
            count_tuple = tuple(count)
            if count_tuple not in res:
                res[count_tuple] = [strs[i]]
            else:
                res[count_tuple].append(strs[i])
        return list(res.values())
            
