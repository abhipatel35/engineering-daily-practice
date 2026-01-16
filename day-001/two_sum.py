class Solution(object):
    def twoSum(nums, target):
        seen = {} # dictionary(number, index) = hashmap(key, value) in java

        for i, num in enumerate(nums): # enumerate(nums) - gives both index and value while iterating.
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i