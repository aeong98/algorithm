def solution(n, times):
    answer = 0
    l=1
    r=n*max(times) # 가장 시간이만이드는 심사관한테 모든 심사를 받은 경우
    while(l<=r):
        people=0
        mid=(l+r)//2 # 전체 소요된 시간
        for time in times:
            people+=mid // time # 심사관 한명 당 맡을 수 있는 사람 수
        if (people >=n): # 심사할 수 있는 사람의 수 > 심사해야 되는 사람의 수 
            answer=mid # 가능하니깐 추가
            # 줄이기 
            r=mid-1
        else:
            # 올리기 
            l=mid+1
    return answer