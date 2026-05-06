class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target
        # nums[j] == target - nums[i]

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                ans = [i, seen[complement]]
                ans.sort()
                return ans
            seen[num] = i
        
        return []