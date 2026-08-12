class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        j = 0
        for num in nums:
            j ^= num
        return j