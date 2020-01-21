"""
两数之和
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for num_1, num_2 in nums:
nums = [2, 4, 7, 15]
target = 9
count = 0
# 用字典模拟哈希求解
hashmap ={}
for key, value in enumerate(nums):
    if hashmap.get(target - value) is not None:
         print(key, hashmap.get(target - value))
    hashmap[value] = key
    print(hashmap)


# 暴力解法 enumerate方法返回序列下标和值
for i, a in enumerate(nums):
    for j, b in enumerate(nums):
        count += 1
        if a + b == target and i < j:
            print(i, j)
        else:
            print(count)

# 暴力解法 range值返回序列长度下标值
for i in range(len(nums)):
    for j in range(len(nums)):
        count += 1
        if nums[i] + nums[j] == target and i < j:
            print(i, j)
            print(count)