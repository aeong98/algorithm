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

function BFS(start, checked, costList, graph){
    var queue=new Queue()
    var start=start
    var max=-1
    checked[start]=true
    queue.add([start,0])
    while (queue.size()>0){
        var tmp=queue.popleft()
        var node= tmp[0]
        var cost = tmp[1]
        costList[node]=cost
        var max=cost >max ? cost : max
        for (var i of graph[node]){
            if(checked[i]==false){
                checked[i]=true
                queue.add([i,cost+1])
            }
        }
    }
    return costList.filter((x)=>x==max).length
}

function solution(n, edge) {
    var graph=[]
    var checked=[]
    var costList=[]
    for (let i=0; i<n+1; i++){
        graph.push([])
        checked.push(false)
        costList.push(0)
    }
    for (let i=0; i<edge.length ; i++){
        var x=edge[i][0]
        var y=edge[i][1]
        graph[x].push(y)
        graph[y].push(x)
    }
   
    
    return BFS(1, checked, costList, graph);
}
