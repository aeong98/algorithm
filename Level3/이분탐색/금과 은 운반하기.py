def solution(a, b, g, s, w, t):
    start=0
    # 최악의 상황 (광물 무게 * 한번에 실어나를 수 있는 무게)*왕복(2) *금은두번(2)
    end = (10 ** 9) * (10 ** 5) * 4
    answer = (10 ** 9) * (10 ** 5) * 4
    
    # 이분탐색
    while start <=end :
        mid = (start + end )//2
        # 현재 옮긴 골드 양
        current_gold=0
        # 현재 옮긴 실버 양
        current_silver=0
        # 같이 옮기는 경우
        total=0
        
        for i, time in enumerate(t):
            # 옮기는 횟수
            cnt = (mid-time) // (time *2) +1
            
            # 옮기게 되는 골드 > 필요한 골드
            current_gold += min(g[i], cnt * w[i])
            current_silver +=min(s[i], cnt * w[i])
            total +=min(cnt*w[i], s[i]+g[i])
        
        # 너무 많이 옮김 -> 줄여도 된다.
        if current_gold >=a and current_silver >=b and total >= a+b:
            end = mid-1
            answer = min(answer, mid)
        else:
            start= mid+1
            
    return answer