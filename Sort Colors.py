class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for x in nums:
            count[x] = count[x] + 1
        idx = 0
        for v in range(3):
            for c in range(count[v]):
                nums[idx], idx = v, idx+1
        return
