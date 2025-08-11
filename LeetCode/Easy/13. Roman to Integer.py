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
            if s[i] in numbers:
               sum += numbers.get(s[i]) 
            i += 1

"""
단순히 더하면 될줄 알았는데 감산규칙? 이라는게 필요하네...
III = 3이지만 IV는 4기때문... 하지만 그냥 더해버리면 IV는 6이 된다... 후...

"""            