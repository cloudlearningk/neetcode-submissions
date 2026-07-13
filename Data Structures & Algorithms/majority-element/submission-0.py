class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max = 0
        answer = None

        for number, count in freq.items():
            if count > max:
                max = count
                answer = number

        return answer        
        