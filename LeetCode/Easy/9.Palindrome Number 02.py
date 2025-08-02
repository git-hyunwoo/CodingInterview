class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            """
            1. if x ends with 0, it can't be palindrome
            2. if x 
            """
            return False
        
        reversed_num = 0
        while x > reversed_num:
            print("==================================")
            print(f"x : {x}")
            print(f"reversed_num : {reversed_num}")
            reversed_num = reversed_num * 10 + x % 10
            print(f"reversed_num * 10 + x % 10 : {reversed_num * 10 + x % 10}")
            x //= 10
            print(f"x //= 10 : {x}")
            print("==================================")
        
        print(f"x[{x}] == reversed_num[{reversed_num}]")
        print(f"x[{x}] == reversed_num // 10[{reversed_num} // 10]")
        return x == reversed_num or x == reversed_num // 10

a = Solution()

print(a.isPalindrome(121))