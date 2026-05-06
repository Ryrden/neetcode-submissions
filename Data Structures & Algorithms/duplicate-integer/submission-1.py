class Solution:
    def hasDuplicate01(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    def hasDuplicate02(self, nums: List[int]) -> bool:
        pass
    def hasDuplicate03(self, nums: List[int]) -> bool:
        pass
    def hasDuplicate(self, nums: List[int]) -> bool:
        return self.hasDuplicate01(nums)
        