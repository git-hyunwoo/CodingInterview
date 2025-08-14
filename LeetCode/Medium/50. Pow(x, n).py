class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 0
        if n < 0:
            # First, convert it to a positive number, calculate the power, and then divide 1 by the result.
            # In Python, you can reverse the sign by adding a minus sign.
            n = -n 
            result = float(1 / (x ** n))
        else:
            result = float(x ** n)
        
        return result
    
a = Solution()
print(a.myPow(2.00, -200000000))