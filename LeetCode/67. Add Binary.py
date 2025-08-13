class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(self.binary_to_decimal(a))
        b = int(self.binary_to_decimal(b))
        return int(self.decimal_to_binary(a + b))
    
    def decimal_to_binary(self, decimal:str) -> str:
        result = ''
        n = int(decimal)

        while n > 0:
            remainder = n % 2
            result = str(remainder) + result
            n = n // 2

        # if answer is empty, return '0' instead
        return result if result else '0'

    def binary_to_decimal(self, binary:str) -> str:        
        result = 0        
        i = 0

        while i < len(binary):
            if binary[i] == '1':
                # Add the power of 2 for the corresponding digit.
                """
                The reason for subtracting `-1` in `(len(binary) - i - 1)` is because the length of the string and the starting point of the index are different. 
                `len(binary)` represents the total number of digits, while the index `i` starts from 0. For example, 
                in a 4-digit binary number `1010`, the leftmost digit (index 0) actually corresponds to the 2^3 place. 
                However, if we calculate using `len(binary) - i`, it would result in 2^4, which is incorrect.
                By subtracting 1, index 0 becomes $2^3$, index 1 becomes $2^2$, index 2 becomes 2^1, and index 3 becomes 2^0, ensuring that the exponent is calculated correctly.
                """
                result += 2 ** (len(binary) - i - 1)
            i += 1

        return str(result)
    
    
a = Solution()#
print(a.addBinary('1010','1011'))
