from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = []
        hit_count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                hit_count += 1
        return hit_count
    
a = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2                
print(a.removeElement(nums,val))
