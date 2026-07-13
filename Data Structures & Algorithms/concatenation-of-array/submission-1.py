class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)

        ans = [0] * (2 * n)

        for num in range(n):
            ans[num] = nums[num]
            ans[num + n] = nums[num]

        return ans    

