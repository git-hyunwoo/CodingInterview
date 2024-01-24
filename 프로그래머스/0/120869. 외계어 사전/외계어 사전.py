def solution(spell, dic):
    answer = 2
    for value in dic:
        cnt = 0
        for s in spell:
            if s in value:
                cnt += 1
        if cnt == len(spell):
            answer = 1
            break
    return answer