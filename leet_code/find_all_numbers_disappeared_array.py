# Exceeds time limit
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ls = []
        ns = sorted(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums:
                ls.append(i)
        return ls

# definitive solution


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
