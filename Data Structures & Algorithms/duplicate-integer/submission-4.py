from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        
        for num in nums:
            counter[num] += 1

        for count in counter.values():
            if count != 1:
                return True
        return False