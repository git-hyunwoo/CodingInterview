class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) # convert Integer type to String
        reversed_x = x[::-1] # reversed String
        if x == reversed_x:
            return True
        else:
            return False


a = Solution()
print(a.isPalindrome(-121))