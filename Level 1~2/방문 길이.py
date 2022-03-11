def solution(dirs):
    answer = 0
		# 방문 경로 중복제거를 위해서 set 사용
    visited=set()
    
    # 시작 (0,0 기준)
    x=0; y=0
    
    # 좌표 1 < 좌표 2 가 보장되어야 한다. (순서 바뀌게 하지 않도록 하기 위해서)
    for di in dirs:
        if di=="U" and y<5:
            visited.add(((x,y), (x,y+1)))
            y+=1
        elif di=="D" and y>-5:
            visited.add(((x,y-1), (x,y)))
            y-=1
        elif di=="R" and x<5:
            visited.add(((x,y), (x+1,y)))
            x+=1
        elif di=="L" and x>-5:
            visited.add(((x-1,y), (x,y)))
            x-=1
    
    
    return len(visited)
