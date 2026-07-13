class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1


        for num in freq.items():
            if num[1] >= 2:
                return True
                
        return False        