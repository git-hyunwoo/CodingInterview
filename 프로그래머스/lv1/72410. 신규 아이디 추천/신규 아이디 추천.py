def solution(new_id):
    answer = ''
    
    user_id = new_id
    
    # stage 1 : Convert every alphabets into lower case
    user_id = new_id.lower()
    print(f'After stage 1 : {user_id}')
    
    # stage 2 : Replace every letter to '' excepts alphabets lower case, numbers, '-','_','.'
    tmp = ''
    for value in user_id:
        
        if isNumber(value):
            tmp += value
        elif value == '-':
            tmp += value
        elif value == '_':
            tmp += value
        elif value == '.':
            tmp += value
        elif ord(value) in range(ord('a'),ord('z') + 1):
            tmp += value
        else:
            tmp += ''
        
    user_id = tmp
    print(f'After stage 2 : {user_id}')
    
    # stage 3 : if there is '..', replace to '.'
    user_id = replace_serial_letter(user_id)
    print(f'After stage 3 : {user_id}')
    
    # stage 4 : if '.' is at the first place or last, get rid of it
    user_id = user_id.strip('.')
    print(f'After stage 4 : {user_id}')    
    
        
    # stage 5 : if string is empty, add 'a'
    if len(user_id) == 0 or user_id == '':
        user_id = 'a'
        
    print(f'After stage 5 : {user_id}')         
        
        
    # stage 6 : if the length of the string is more than 16, replace it from 1~15
    # and if the last or first letter is . , replace it to ''
    if len(user_id) >= 16:
        user_id = user_id[:15]
        
    user_id = user_id.strip('.')
    
    print(f'After stage 6 : {user_id}')     
        
    # stage 7 : if the length of the string is less than 2, mulitple last letter for 3 times
    if len(user_id) <= 2:
        while len(user_id) != 3:
            user_id += user_id[-1]
        
    print(f'After stage 7 : {user_id}')         
    
    
    answer = user_id
    
    return answer

def isNumber(letter):
    
    """
    if the given parameter is number,
    return True, else return False
    """
    
    flag = False
    
    numbers = [
        '0','1','2','3','4',
        '5','6','7','8','9',
    ]
    
    if letter in numbers:
        flag = True
        
    return flag


def replace_serial_letter(user_id):
    # 2번 이상 연속된 문자열 변환하는 함수
    tmp = []
    last_in_is_dot = False
    for value in user_id:
        
        if value == '.' and not last_in_is_dot:
            tmp.append(value)
            last_in_is_dot = True
        
        if value == '.' and last_in_is_dot:
            continue
        else:
            tmp.append(value)
            last_in_is_dot = False
    
    tmp = ''.join(tmp)
        
    return tmp
