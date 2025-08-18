class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = []
        tmp = ''
        for v in s:
            if v != '' and v != ' ':
                tmp += v   
            else:
                print(f' => {tmp}')
                if tmp != '':
                    lst.append(tmp)
                tmp = ''

        if tmp != '':
            lst.append(tmp)
        # To get rid of '' in lst
        #lst = [v for v in lst if v != '']

        return len(lst[-1])
    
a = Solution()
print(a.lengthOfLastWord('luffy is still joyboy'))