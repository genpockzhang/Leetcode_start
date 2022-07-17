class Solution:
    # 暴力解法
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

    # 哈希表
    def twoSum_2(self, nums, target):
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i
        return []

