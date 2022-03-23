function solution(n, times){
    answer=0
    l=1
    max=-1
    for (var time of times){
        max=Math.max(time, max)
    }

    while(l<=r){
        people=0
        mid=parseInt((l+r)/2)
        for (var time of times){
            people+=parseInt(mid/time)
        }
        if(people>=n){
            answer=mid
            r=mid-1
        }
        else{
            l=mid+1
        }
    }
    return answer
}