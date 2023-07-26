def solution(nums):
    answer = 0
    
    lst = []
    
    for num in nums:
        if num not in lst:
            lst.append(num)
    
    if len(lst) <= len(nums) / 2:
        answer = len(lst)
    else:
        answer = len(nums) / 2
        
    return answer