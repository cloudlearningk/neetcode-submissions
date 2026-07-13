class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i,num in enumerate(nums):

            compliement = target - num

            if compliement in map:
                return [map[compliement] , i]

            map[num] = i 