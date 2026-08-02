class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for num in nums:
            if num not in data:
                data[num] = 1
            else:
                data[num] += 1

        for num, val in data.items():
            if val > 1:
                return True
        
        return False