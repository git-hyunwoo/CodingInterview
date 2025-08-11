from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary search on a sorted (non-decreasing) list.

        Loop invariant (always true at the start of each iteration)
          - If target exists, it must be within the inclusive window [left, right].
          - All indices < left hold values strictly less than target.
          - All indices > right hold values strictly greater than target.
        These facts justify how we shrink the window and why 'left' becomes the
        correct insertion index when the loop ends.
        """
        left, right = 0, len(nums) - 1  # Start with the full inclusive window; every index is a candidate.

        while left <= right:  # Keep searching while there is at least ONE candidate index left (left==right is still a valid single candidate).
            # Use floor division so 'mid' is an integer index.
            # This form also avoids overflow in fixed-width integer languages (not an issue in Python, but good practice).
            mid = (left + right) // 2

            # Single comparison splits the window into three disjoint cases relative to target.
            if nums[mid] == target:
                # Exact match: the spec allows returning any matching index.
                # Safe because the invariant guarantees 'mid' is inside the candidate window.
                # Note: If you needed the first occurrence for duplicates ("lower_bound"),
                # you would NOT return here; you'd set right = mid - 1 and continue.
                return mid
            elif nums[mid] < target:
                # Everything at or left of 'mid' is <= nums[mid] < target,
                # so none of indices [left..mid] can hold the target.
                # Move the start just past 'mid' to strictly shrink the window and ensure progress.
                left = mid + 1
            else:
                # nums[mid] > target
                # Everything at or right of 'mid' is >= nums[mid] > target,
                # so none of indices [mid..right] can hold the target.
                # Move the end just before 'mid' to strictly shrink the window and ensure progress.
                right = mid - 1

        # Window exhausted: now right < left (the inclusive window is empty).
        # By the invariant
        #   - all indices < left have values < target
        #   - all indices >= left have values >= target
        # Therefore, 'left' is exactly the position to insert 'target' to keep the list sorted
        # (i.e., the lower_bound insertion index).
        return left

print(Solution().searchInsert([1,2,3,4,5,6,7,8,9,10], 7))
