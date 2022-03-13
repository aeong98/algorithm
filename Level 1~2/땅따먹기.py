def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[i])):
					 # 이전 행에서 자신의 열을 제외한 원소중 가장 큰 원소 선택해 더하면 된다.
            land[i][j]+=max(land[i-1][:j]+land[i-1][j+1:])
    
    
    return max(land[-1])
