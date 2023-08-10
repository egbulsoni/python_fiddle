# Bad solution, O(n**2)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            return [i, hash_map[nums[i]]]
        else:
            hash_map[target - nums[i]] = i

# Most efficient


def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            return [i, hash_map[nums[i]]]
        else:
            hash_map[target - nums[i]] = i


# sample data: [0,1,3] target 4
# 0 in hash_map? no
# hash_map[4 - 0] = 0
# hash_map[4] = 0
# 1 in hash_map? no
# hash_map[4 - 1] = 1
# hash_map[3] = 1
# 3 in hash_map? yes
# return [2, hash_map[3]]
# return [2, 1]
