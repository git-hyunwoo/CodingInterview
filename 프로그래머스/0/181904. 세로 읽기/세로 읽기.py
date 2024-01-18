"""
Writer : Jack Snider
Date : 2024.01.18
Thought : It was bit hard for me to understand how to slice the array with list comprehension
"""
def solution(my_string, m, c):
    answer = ''
    sliced_strings = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    for value in sliced_strings:
        if c == 1:
            answer += value[0]
        else:
            answer += value[c - 1]
    return answer