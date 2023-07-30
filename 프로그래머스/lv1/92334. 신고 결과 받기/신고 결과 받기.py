def solution(id_list, report, k):
    answer = [0] * len(id_list) # 정답으로 제출할 리스트를 만들기 위해 id_list의 길이만큼 0으로 초기화
    print(f'answer : {answer}') # answer : [0, 0, 0, 0]
    
    reported = {x:0 for x in id_list} # 각 유저가 신고당한 횟수를 저장하기 위한 dictionary 초기화
    print(f'reported : {reported}') # reports : {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
    
    for report_case in list(set(report)): # 중복으로 신고된건 일단 다 제외
        # 신고당한 유저의 아이디가 dictionary의 key값으로 있으면 해당 value를 1씩 증가
        reported_person = report_case.split()[1]
        reported[reported_person] += 1 
    
    print(f'reported : {reported}')
    
    for report_case in list(set(report)):
        # 각 유저가 신고당한 횟수가 k번 이상이면 정지
        reporter = report_case.split()[0] # 신고한 사람
        reported_person = report_case.split()[1] # 신고당한 사람
        if reported[reported_person] >= k: # 신고당한 횟수가 k번 이상이면 정지
            answer[id_list.index(reporter)] += 1  
        
    print(f'Final answer : {answer}')
    
    return answer