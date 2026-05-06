class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        for num in nums:
            curr += num
            maxSum = max(curr, maxSum)
            curr = max(curr, 0)
        return maxSum