function solution(n, edge){
    // 길이가 n+1인 이차원 배열 만들기
    const graph=Array.from(Array(n+1), ()=>[]);

    // graph 간선 정보 저장
    for (const [src, dest] of edge){
        grpah[src].push(dest);
        graph[dest].push(src);
    }

    // 거리 저장 리스틑 초기화 
    const distance = Array(n+1).fill(0);
    distance[1]=1


    // BFS
    const queue=[1];
    while (queue.length > 0){
        const src= queue.shift(); // shift 는 O[n] 이지만 요소가 적을 경우에는 자바스크립트 엔진에서 최적화를 해줌.
        for (const dist of graph[src]){
            if (distance[dist]==0){
                queue.push(dist);
                distance[dist]=distance[src]+1;
            }
        }
    }

    const max=Math.max(...distance);
    return distance.filter(item=>item===max).length
}