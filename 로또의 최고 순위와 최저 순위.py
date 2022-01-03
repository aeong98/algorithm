def solution(lottos, win_nums):
    answer = [];
    match_cnt=0;
    zero_cnt=0;
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            match_cnt+=1;
        elif lottos[i]==0:
            zero_cnt+=1;
    
    # 최상의 시나리오 : match_cnt + zero_cnt 다 맞았을 때,
    if(match_cnt+zero_cnt>=2):
        answer.append(7-(match_cnt+zero_cnt));
    else:
        answer.append(6);
    # 최악의 시나리오 : match_cnt 를 뺀 나머지 zero_cnt 가 다 틀렸을 때,
    if(match_cnt>=2):
        answer.append(7-match_cnt);
    else:
        answer.append(6);
    return answer
