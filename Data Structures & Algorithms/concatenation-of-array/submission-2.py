class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        for i in range(n * 2):
            answer.append(nums[i % n])

        return answer