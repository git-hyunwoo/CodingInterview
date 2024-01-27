def solution(num_list):
    answer = 0
    
    for number in num_list:
        count = 0
        while number != 1:
            if number % 2 == 0:
                number = number / 2
                count += 1
            else:
                number = number - 1
                number = number / 2
                count += 1
                
        answer += count
        
    return answer