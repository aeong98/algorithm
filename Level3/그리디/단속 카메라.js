function solution(routes) {
    // 첫 차량 카메라 설치 
    var answer = 1
    
    // 진입시점을 기준으로 오름차순 정렬 (먼저 들어온 것부터)
    routes.sort((a,b) => a[0]-b[0])
    
    // 첫 차량의 진출 시점.
    let out= routes[0][1]

    for (const [this_in, this_out] of routes){
        // 이전 차량의 진출 시점보다 현재 차량의 진입이 느리다면
        // 카메라 추가 설치 및 out 시점 갱신
        if(out < this_in){
            answer++;
            out=this_out
        }
        
        // 이전 차량의 진출 시점이 현재 차량의 진출 시점보다 큰 경우
        // out 갱신, 카메라 설치 X 
        if(out > this_out){
            out = this_out 
        }
        
    }
    return answer;
}
