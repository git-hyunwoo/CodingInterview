def solution(my_string):
    answer = ''
    
    lst = ['a','e','i','o','u']
    for value in my_string:
        if value in lst:
            my_string = my_string.replace(value,'')
    
    answer = my_string
    
    return answer