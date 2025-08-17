class Solution:
    def maximum69Number (self, num: int) -> int:

        # If given number num contains only 9
        if all(v =='9' for v in str(num)):
            return num

        lst = []
        for i,v in enumerate(str(num)):
            n = list(str(num))
            if v == '9':
                n[i] = '6'
                lst.append(''.join(n))
            else:
                n[i] = '9'
                lst.append(''.join(n))
        
        return max([int(v) for v in lst])


a = Solution()        
print(a.maximum69Number(9669))
            
    
