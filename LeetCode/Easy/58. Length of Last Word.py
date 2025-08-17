class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = []
        tmp = ''
        for v in s:
            if v != '' and v != ' ':
                tmp += v    
            else:
                if tmp != '':
                    lst.append(tmp)
                tmp = ''

        # To get rid of '' in lst
        #lst = [v for v in lst if v != '']
        
        return len(lst[-1])
    
a = Solution()
print(a.lengthOfLastWord('   fly me   to   the moon  '))