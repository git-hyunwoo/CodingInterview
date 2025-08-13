from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # If empty list has been given, return ""
        if not strs:
            return ''
        
        min_length = min(len(s) for s in strs)
        print(f"min_length : {min_length}")
        
        i = 0
        result = ''
        while i < min_length:
            tmp = []
            for s in strs:
                tmp.append(s[i])
                
            if all(t == tmp[0] for t in tmp):
                result += tmp[0]
            else:
                break      
                       
            i += 1
        
        return result
        
obj = Solution()
#strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(obj.longestCommonPrefix(strs))
