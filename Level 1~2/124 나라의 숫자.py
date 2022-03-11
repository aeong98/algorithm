def solution(n):
    # n이 3보다 작아졌을 때는, 3진법으로 바꾸지 않고 바로 추출
    if n<=3:
        return '124'[n-1]
    # 그외에는 3진법으로 추출, 0이 없기 때문에 n-1
    else:
        q,r=divmod(n-1,3)
        return solution(q)+'124'[r]
