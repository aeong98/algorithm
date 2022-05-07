// 플로이드 와샬 
function solution(n, s, a, b, fares) {
    // 플로이드 와샬 - 모든 정점에서 각각의 정점으로 가는 최단 경로
    // 왜 각각의 정점에서 각각의 정점으로 향하는 최단경로 필요?
    
    // n개 노드에 대해 모든 정점(n개) 로 향하는 DP 배열
    const board = new Array(n).fill().map(_ => new Array(n).fill(Infinity));
    
    // 자기 자신에 대한 최단 경로는 0으로 설정
    for(let i=0; i<n ; i++){
        board[i][i]=0;
    }
    
    // 주어진 연결 정보로 DP 배열 초기화
    for (const [x,y,weight] of fares){
        board[x-1][y-1]=weight;
        board[y-1][x-1]=weight;
    }
    
    //k는 경유 노드, i는 시작노드, j는 도착노드
    for(let k = 0; k < n; k++) {
      for(let i = 0; i < n; i++) {
        for(let j = 0; j < n; j++) {
          if(board[i][k] + board[k][j] < board[i][j])
            board[i][j] = board[i][k] + board[k][j];
        }
      }
    }
    
    // 각자 따로가는 경우
    let answer = board[s-1][a-1] + board[s-1][b-1];
    
    // 마지막 합승지점 하나씩 돌면서 더 최단거리 있는지 확인
    for(let i = 0; i < n; i++) {
        const shortest = board[s-1][i] + board[i][a-1] + board[i][b-1];
        answer = Math.min(answer, shortest);
      }
    
    return answer
  
}
