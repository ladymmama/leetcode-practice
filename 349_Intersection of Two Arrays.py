class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TC: O(n+m) SC:(1)
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set()
        res = []
        for i in range(len(nums1)):
            lookup.add(nums1[i])

        for j in range(len(nums2)):
            if nums2[j] in lookup:
                res.append(nums2[j])
                lookup.discard(nums2[j])

        return res