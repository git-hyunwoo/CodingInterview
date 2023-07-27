def solution(str1, str2):
    answer = ''
    if len(str1) == len(str2):
        for idx in range(len(str1)):
            answer += str1[idx] + str2[idx]
    else:
        raise TypeError("WRONG!")
    return answer