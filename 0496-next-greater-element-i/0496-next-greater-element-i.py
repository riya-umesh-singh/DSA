class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        ngreat = {}

        for i in range(len(nums2) - 1, -1, -1):
            curr = nums2[i]

            while stack and stack[-1] <= curr:
                stack.pop()

            if not stack:
                ngreat[curr] = -1
            else:
                ngreat[curr] = stack[-1]

            stack.append(curr)

        ans = []

        for num in nums1:
            ans.append(ngreat[num])

        return ans
        