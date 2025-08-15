class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base, exp):
            if exp == 0:  # If the exponent is 0, the result is 1 regardless of the base.
                return 1
            half = fast_pow(base, exp // 2)  # Recursively calculate by halving the exponent.
            if exp % 2 == 0:  # If the exponent is even, square it as is.
                return half * half
            else:  # If the exponent is odd, multiply by the base once more.
                return half * half * base
        
        if n < 0:  # If the exponent is negative, return the reciprocal.
            return 1 / fast_pow(x, -n)
        else:
            return fast_pow(x, n)
    
a = Solution()
print(a.myPow(2.00, -200000000))

"""

찾아보니 문제를 풀기 위해선 빠른 거듭제곱 방법을 사용해아하고 시간복잡도는 O(log n)이 나와야한다고 한다.
즉, 한 번 연산할떄마다 수행해야할 연산 횟수가 절반씩 줄어들어야한다.

예를들어 2^8을 하려면 2 x 2 x 2 x 2 x 2 x 2 x 2 x 2를 해야한다 그지? 즉, n번만큼 연산을 수행해야하므로
O(n)의 시간복잡도를 가지게된다. 

하지만 2^8은 다른 의미로 2^4 x 2^4라고 할 수 있다. 그리고 2^4는 2^2 * 2^2로 다시 할 수 있다.

"""