class Queue {
    constructor() {
      this.storage = {};
      this.front = 0;
      this.rear = 0;
    }
    
    size() {
      if (this.storage[this.rear] === undefined) {
        return 0;
      } else {
        return this.rear - this.rear + 1;
      }
    }
    
    add(value) {
      if (this.size() === 0) {
        this.storage['0'] = value;
      } else {
        this.rear += 1;
        this.storage[this.rear] = value;
      }
    }
    
    popleft() {
      let temp;
      if (this.front === this.rear) {
        temp = this.storage[this.front];
        delete this.storage[this.front];
        this.front = 0;
        this.rear = 0;
      } else {
        temp = this.storage[this.front];
        delete this.storage[this.front];
        this.front += 1;
      }
      return temp;
    }
  }
  
  function solution(m) {
      var answer = 0;
      // dp 에 cnt 저장
      const dp = Array.from(Array(m.length+1), ()=>0);
      find(0,m, dp)
      return answer;
  }
  
  
  // BFS 최단거리
  function find(start, m, dp){
      if(dp[start] !== 0){
          console.log(dp[start])
          return 
      }
      if(start<0){
          start =0
      }
      // start > 8 이면 start =8
      if(start>8){
          start =8
      }
      // 8이면 return
      if(start === 8){
          console.log(dp[start])
          return dp[start]
      }
      
      // 만약에 숫자= 0 이라면 다시굴림 (1~6) cnt +1
      if(m[start]=== 0){
          console.log(dp[start])
  
          for (let i=1; i<=6; i++){
              // 만약 dp[i] 가 0 이 아니고, dp[start]+1 보다 작다. 그럼 안감. break
              // 아니면 방문하고 dp[start+i] = dp[start]+1 로 갱신
              if(dp[start+i]!==0 && dp[start+i] < dp[start]+1){
                  return '안감'
              }
              else{
                  dp[start+i]=dp[start]+1
                  find(start+i, m, dp)
              }
              
          }
      }
      // 숫자 > 0  이라면 그만큼 왼쪽이동 이동
      else if(m[start] >0){
          if(dp[start+m[start]]!==0 && dp[start+m[start]] < dp[start]+1){
              return '안감'
          }
          dp[start+m[start]]=dp[start]+1
          find(start+m[start], m , dp)
      }
      else{
          if(dp[start+m[start]]!==0 && dp[start+m[start]] < dp[start]+1){
              return '안감'
          }
          dp[start+m[start]]=dp[start]+1
          find(start+m[start], m , dp)
      }
  
  }