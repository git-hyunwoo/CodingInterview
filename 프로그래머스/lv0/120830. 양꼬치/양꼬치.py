def solution(n, k):
    answer = 0
    
    # 양꼬치 n개
    # 음료수 k개
    
    beverage_discount_price = (n // 10) * 2000
    answer = ((n * 12000) + (k * 2000)) - beverage_discount_price
        
    
    
    return answer