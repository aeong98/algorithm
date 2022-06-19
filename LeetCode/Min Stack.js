
var MinStack = function() {
     this.stack=[];
     this.minEl;
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
   
    if(this.stack.length === 0){
        this.stack.push(val);
        this.minEl=val;
        return; 
    }   
    else if(val < this.minEl){
        // val보다 작은 원소로 집어넣기
        this.stack.push(2*val -this.minEl);
        this.minEl=val;
    }
    else{
        this.stack.push(val);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    if(this.stack.length === 0){
        return null;
    }
    
    const topItem = this.stack[this.stack.length -1]
    this.stack = this.stack.slice(1,this.stack.length-1);
    
    // 지금 minEl 이 top 에 있다는 뜻.
    if(topItem < this.minEl){
        let result = this.minEl;
        // 기존 데이터로 minEl 갱신해주기
        this.minEl= 2*this.minEl -topItem;
        return result;
    }
    else{
        return topItem;
    }
    
    
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length-1]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.minEl;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
