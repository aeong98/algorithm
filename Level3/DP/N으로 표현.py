def solution(N, number):
    answer=0
    flag=0
    if N==number:
        return 1
    
    # N 반복횟수 저장을 위한 집합 초기화 (DP)
    # dp[i]= N을 i개 가지고 사칙연산 했을 때 때 만들 수 있는 set
    dp=[set() for _ in range(8)]
    
    # 각 set 마다 기본 수 "N" * i 초기화
    for i, x in enumerate(dp, start=1):
        x.add(int(str(N) * i))

    print(dp)
        
    # n 일반화 
    # i : N을 i 개 가지고 사칙연산했을 때
    for i in range(1,8):
        # j: 0~i-1까지 반복문 순회
        for j in range(i):
            # j : N을 j번 써서 만들수 있는 숫자 SET
            for x in dp[j]:
                # x : N을 i-j-1 써서 만들 수 있는 숫자 SET
                for y in dp[i-j-1]:
                    # 사칙연산 수행
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y!=0:
                        dp[i].add(x//y)
                        
        # i번써서 만든 숫자 집합에 number 있을 때
        # 0부터 인덱스 사용했기 떄문에 i+1 리턴
        if number in dp[i]:
            answer =i+1
            flag=1
            break
            
    if(flag==0): answer= -1
    
            
    return answer
