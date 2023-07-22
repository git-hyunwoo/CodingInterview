def solution(s):
    answer = []
    
    s = s.split(' ')
    """
    split()과 split(' ')의 차이
    s = "  try hello world   "
    s.split() → ['try', 'hello', 'world']
    s.split(' ') → ['', '', 'try', 'hello', 'world', '', '', '']
    """
    for word in s:        
        tmp_word = ''
        for w in range(0,len(word)):
                
            if w % 2 == 0:
                # 짝수일 경우 → 대문자
                tmp_word += word[w].upper()
            else:
                # 홀수일 경우 → 소문자
                tmp_word += word[w].lower()

        answer.append(tmp_word)
    
    answer = ' '.join(answer)
    
    
    return answer
