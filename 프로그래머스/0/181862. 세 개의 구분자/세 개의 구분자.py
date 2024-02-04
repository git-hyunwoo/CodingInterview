import re
def solution(myStr):
    answer = [s for s in re.split('[a, b, c]', myStr) if s]
    
    return answer if answer else ["EMPTY"]
    
    return answer