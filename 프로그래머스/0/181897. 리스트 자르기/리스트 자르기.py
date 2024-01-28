def solution(n, slicer, num_list):
    answer = []
    
    a,b,c = ' '.join(map(str,slicer)).split(' ')
    a,b,c = int(a), int(b), int(c)
    
    if n == 1:
        answer = num_list[:b + 1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b + 1]
    elif n == 4:
        answer = num_list[a:b + 1:c]
    else:
        print('n은 1~4중 하나입니다.')
    
    return answer