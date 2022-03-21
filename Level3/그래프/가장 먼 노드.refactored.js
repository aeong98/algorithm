class Queue{
    constructor(){
        this.queue=[];
        this.front=0;
        this.rear=0;
    }

    enqueue(value){
        this.queue[this.rear++]=value;
    }

    dequeue(){
        const value=this.queue[this.front];
        delete this.queue[this.front];
        this.front+=1;
        return value;
    }

    isEmpty(){
        return this.rear===this.front;
    }
}




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
    const queue=new Queue();
    queue.enqueue(1)
    while (queue.isEmpty()){
        const src= queue.dequeue(); 
        for (const dist of graph[src]){
            if (distance[dist]==0){
                queue.enqeueu(dist);
                distance[dist]=distance[src]+1;
            }
        }
    }

    const max=Math.max(...distance);
    return distance.filter(item=>item===max).length
}