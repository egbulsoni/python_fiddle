class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        z = -1
        for i in range(len(nums)):
            if (nums[i] == 0):
                z = i
                continue
            prod *= nums[i]

        if (nums.count(0) > 1):
            prod = 0

        for i in range(len(nums)):
            if (z >= 0):
                if (nums[i] != 0):
                    nums[i] = 0
                else:
                    nums[i] = prod
            else:
                if (nums[i] != 0):
                    nums[i] = int(prod / nums[i])
                else:
                    nums[i] = int(prod)
        return nums


# [0,1,2,3]
# [1*2*3, 0*2*3, 0*1*3, 0*1*2]
# sample data
# [0,0]
