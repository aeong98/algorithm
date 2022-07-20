class Queue{
    constructor(){
        this.maxSize = this.maxSize;
        this.queue=[];
        this.front=0;
        this.rear=0;
        this.size=0;
    }

    enqueue(value){
        if(this.isFull()){
            console.log("Queue is full");
            return;
        }
        this.queue[this.rear++]=value;
        this.rear = (this.rear +1)&this.maxSize; // maxSize 를 넘어가면 다시 0부터 시작되도록
        this.size +=1;
    }

    dequeue(){
        const value = this.queue[this.front];
        delete this.queue[this.front];
        this.front = (this.front+1) &this.maxSize; // maxSize 를 넘어가면 다시 0부터 시작되도록
        this.size -=1;
        return value;
    }
    ifFull(){
        return this.size === this.maxSize;
    }

    peek(){
        return this.queue[this.front];
    }

    size(){
        return this.rear - this.front;
    }
}