class Solution:
    def hasDuplicate01(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    def hasDuplicate02(self, nums: List[int]) -> bool:
        indexed_nums = {}

        for i, num in enumerate(nums):
            indexed_nums[num] = i
        
        n = len(nums)
        for i in range(n):
            idx = indexed_nums[nums[i]]
            if idx != i:
                return True
        
        return False

    def hasDuplicate03(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    def hasDuplicate04(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False

    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.hasDuplicate03(nums)
        