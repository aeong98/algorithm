def solution(rows, columns, queries):
    answer = []
    # 행렬 만들기
    table = []
    for r in range(rows):
        # 행들을 열의 개수만큼 만들기
        table.append([a for a in range(r*columns+1,(r+1)*columns+1)])
        
    
    # 테두리 시계방향으로 한 칸씩 옮기기 (단순 구현)
    for query in queries:
        # 0 부터 시작하기 때문에 -1 씩 해준다.
        query = [x-1 for x in query]
        # 왼쪽 위 값 저장 (밀면 맨 왼쪽 위에 있던 값을 잃게 되기 때문에 : 마지막에 원래 위치의 오른쪽에 넣어준다.)
        start = table [query[0]][query[1]]
        # 가장 작은 값 초기화
        small=start
        
        # left 
        for i in range (query[0]+1, query[2]+1):
            table[i-1][query[1]]= table[i][query[1]]
            small=min(small, table[i][query[1]])
        # bottom
        for i in range (query[1]+1, query[3]+1):
            table[query[2]][i-1]=table[query[2]][i]
            small=min(small,table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1,-1):
            table[i+1][query[3]]=table[i][query[3]]
            small=min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1]=table[query[0]][i]
            small=min(small,table[query[0]][i])
        # 시작지점 오른쪽에 start 추가
        table[query[0]][query[1]+1]=start

        answer.append(small)

        
    return answer
