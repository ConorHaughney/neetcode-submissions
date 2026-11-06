class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for elt in nums:
            if not mp[elt]:
                mp[elt] = mp[elt - 1] + mp[elt + 1] + 1
                mp[elt - mp[elt - 1]] = mp[elt]
                mp[elt + mp[elt + 1]] = mp[elt]
                res = max(res, mp[elt])
        
        return res
