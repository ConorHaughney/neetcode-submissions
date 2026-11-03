class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for elt in strs:
            count = [0] * 26
            for c in elt:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(elt)

        return list(res.values())