def solution(arr1, arr2):
    
    sum = []
    
    tmp = 0
    for value in arr1:
        tmp += value
    sum.append(tmp)
    
    tmp = 0
    for value in arr2:
        tmp += value
    sum.append(tmp)
    
    if len(arr1) == len(arr2):
        if sum[0] == sum[1]:
            answer = 0
        elif sum[0] > sum[1]:
            answer = 1
        else:
            answer = -1
    elif len(arr1) > len(arr2):
        answer = 1
    else:
        answer = -1
    
    return answer