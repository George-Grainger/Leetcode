class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen = 0
        for el in nums:
            if el != val:
                nums[seen] = el
                seen += 1
        return seen