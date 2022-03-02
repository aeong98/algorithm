from itertools import combinations
def solution(line):
    # 직선 조합 구하기
    dots =[]
    for x, y in list(combinations(line,2)):
        denominator = x[0]*y[1]-x[1]*y[0]
        if(denominator==0): continue
        a= (x[1]*y[2]-x[2]*y[1])/denominator
        b=(x[2]*y[0]-x[0]*y[2])/denominator
        if (a-int(a)==0 and b-int(b)==0):
            a=int(a)
            b=int(b)
            dots.append((a,b))
        else:
            continue
    
    # 중복제거
    dots=list(set(dots))
    
    # 사각형 크기를 구하기 위한 좌표 최대, 최솟값 구하기
    x_dots=[d[0] for d in dots]
    x_min=min(x_dots)
    x_max=max(x_dots)
    
    y_dots=[d[1] for d in dots]
    y_min=min(y_dots)
    y_max=max(y_dots)
        
    answer = ['.' * (x_max-x_min+1) ]* (y_max-y_min+1)
    # 각 좌표마다 * 그리기
    for dot in dots:
        x,y=dot
        answer[y_max-y]=answer[y_max-y][:x-x_min]+'*'+answer[y_max-y][x-x_min+1:]
        
    return [''.join(ans) for ans in answer]
