class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}                                # ans record the NGE of every num in nums2 if exists.
        res = []
        stack = []                              # Using decreasing stack to find NGE.
        
        for n2 in nums2:
            while stack and n2 > stack[-1]:     # At this situation, n2 is the NGE of stack[-1],
                ans[stack.pop()] = n2           # so map stack[-1] to n2.
            stack.append(n2)
		# [4, 2] {1: 3, 3: 4}
        
        for n1 in nums1:                        # Iterate through nums1,
            res.append(ans.get(n1, -1))         # if n1 not appear in ans, there isn't NGE for n1, res.append(-1).
                                                # Otherwise, res.append(ans[n1])
        
        return res
