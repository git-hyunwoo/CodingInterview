class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and numbers.get(s[i]) < numbers.get(s[i + 1]):
                # 1) i + 1 < len(s): Check if there is a next character to avoid index out-of-range errors
                # 2) numbers[s[i]] < numbers[s[i + 1]]:
                #    If the current value is smaller than the next value, apply the Roman numeral subtraction rule
                #    Examples: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
                sum += numbers.get(s[i + 1]) - numbers.get(s[i])
                i += 2
            else:
                sum += numbers.get(s[i]) 
                i += 1

        return sum
