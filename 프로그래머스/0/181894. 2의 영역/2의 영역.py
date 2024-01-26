def solution(arr):
    answer = []
    
    stored_index = []
    
    for index, value in enumerate(arr):
        if value == 2:
            stored_index.append(index)
            
    if len(stored_index) == 0:
        answer = [-1]
    elif len(stored_index) == 1:
        index = stored_index[0]
        answer.append(arr[index])
    else:
        min_index = min(stored_index)
        max_index = max(stored_index)
        answer = arr[min_index : max_index + 1]
    
    return answer