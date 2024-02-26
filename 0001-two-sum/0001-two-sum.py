class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={} #value:index
        for i,val in enumerate(nums):
            if target-val in hashtable:
                return [i,hashtable[target-val]]
            hashtable[val]=i