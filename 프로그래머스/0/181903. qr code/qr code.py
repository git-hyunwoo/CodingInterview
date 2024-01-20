"""
Writer : Jack Snider
Date : 2024.01.20
"""
def solution(q, r, code):
    answer = '' 
    for index, value in enumerate(code):
        if index % q == r:
            answer += value
    return answer