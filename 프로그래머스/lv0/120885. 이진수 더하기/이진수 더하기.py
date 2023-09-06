def solution(bin1, bin2):
    bin1 = int(bin1,2)
    bin2 = int(bin2,2)

    answer = str(bin(bin1 + bin2))
    answer = answer.replace("0b","")
    return answer