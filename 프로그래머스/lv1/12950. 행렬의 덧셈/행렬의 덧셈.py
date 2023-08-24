def solution(arr1, arr2):
    answer = []
    
    for a,b in zip(arr1,arr2):
        tmp = []
        for i,j in zip(a,b):
            tmp.append(i + j)        
        answer.append(tmp)
    
    return answer