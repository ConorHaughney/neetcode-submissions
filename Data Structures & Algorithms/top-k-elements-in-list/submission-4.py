class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for elt in nums:
            count[elt] = 1 + count.get(elt,0)

        for elt, cnt in count.items():
            freq[cnt].append(elt)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for elt in freq[i]:
                res.append(elt)
                if len(res) == k:
                    return res