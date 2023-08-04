def solution(my_string):
    answer = 0

    numbers = extract_number(my_string)

    for value in numbers:
        answer += value
    
    return answer

def extract_number(my_string):
    
    numbers = ['0','1','2','3','4',
               '5','6','7','8','9',
              ]
    
    lst = []
    
    for value in my_string:
        if value in numbers:
            lst.append(int(value))
            
    return lst