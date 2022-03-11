def solution(progresses, speeds):
    # answer : 각 배포마다 배포되는 기능의 수가 적힌 정수 배열
    answer = [];
    # days: 배포일
    days=1;
    # cnt : 오늘 배포되는 기능의 수
    cnt =0 ;
    # progress : 현재 기능의 작업 진도
    progress =0;
    while(len(progresses)>0):
        # 첫 번째 기능의 작업 진도
        progress = progresses [0] + (speeds[0] * days);     # 첫 번째 기능의 작업 진도가 100 이상인 경우 배포 완료
        if(progress >=100):
            # 배포 완료된 기능 개수 추가
            cnt+=1;
            # 배포 완료된 작업 제거
            progresses.pop(0);
            # 배포 완료된 작업의 속도 제거
            speeds.pop(0);
        
        # 첫 번째 기능의 작업 진도가 100 미만일 경우 배포 불가능
        else:
            # 배포 완료된 기능이 있는 경우, answer 에 push
            if(cnt >0):
                answer.append(cnt);
            
            # 배포일 증가 (다음날)
            days +=1;
            # 배포 완료된 기능 개수 초기화
            cnt =0;
            
        
    # 모든 작업이 다 배포되고 나면, 마지막으로 카운트된 배포 완료 기능 개수 push
    answer.append(cnt);
    return answer
