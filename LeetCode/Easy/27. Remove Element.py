from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for v in nums:
            if v != val:
                nums[k] = v 
                k += 1 # 
        return k


