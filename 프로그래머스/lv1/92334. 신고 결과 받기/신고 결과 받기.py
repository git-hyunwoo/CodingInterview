def solution(id_list, report, k):
    answer = []
    
    dictionary = {}
    
    for user in id_list:
        reported_people_by_user = []    
        for report_case in report:
            reporter,reported = report_case.split(' ')
            if user in reporter: # user가 신고한 내역이 있으면
                reported_people_by_user.append(reported) # user가 신고한 사람의 아이디를 저장
                
        if dictionary.get(user) == None:
            dictionary[user] = reported_people_by_user
           
    banned_list = [] # 정지당한 사람 리스트
    
    # 정지당한 사람들 목록 만들기
    for user in id_list:
        reported_count = 0
        for key,value in dictionary.items():
            if user in value:
                reported_count += 1
        if reported_count >= k:
            banned_list.append(user)
      
    # 정지당한 아이디가 유저가 신고한 목록(dictionary)에 있으면...
    for key,value in dictionary.items():
        count = 0
        for reported_person in value:
            if reported_person in banned_list:
                count += 1
            
        answer.append(count)
    
    return answer