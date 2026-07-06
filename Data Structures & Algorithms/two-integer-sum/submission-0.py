class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_memo = {}
        answer = []

        for index, number in enumerate(nums):
            needed_number = target - number
            if needed_number in nums_memo:
                return [nums_memo[needed_number], index]
            nums_memo[number] = index

