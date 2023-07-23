def solution(n):

    dictionary = {
        '0':'zero',
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine',
    }
    
    for key,value in dictionary.items():
        if value in n:
            n = n.replace(value,key)
    
    answer = n

    return int(answer)

