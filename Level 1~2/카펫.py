def solution(brown, yellow):
    # 사각형 전체 넓이
    total=brown+yellow;
    # 전체 넓이부터 거꾸로 완전탐색 (yellow는 1이상이기 때문에, 한 변의 길이는 무조건 3이상)
    for x in range(total,2,-1):
        # 나누어 떨어지면 x는 가능한 변
        if total % x ==0:
            # y 는 total 을 x로 나눈 것
            y=total//x
            # 만약 yellow 의 넓이가 -2해서 곱한 넓이와 같다면
            if(yellow== (x-2)*(y-2)):
                # 정답
                return [x,y]
