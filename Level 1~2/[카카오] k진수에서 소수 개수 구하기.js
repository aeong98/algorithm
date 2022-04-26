function solution(n, k) {
    return n.toString(String(k))
        .split("0")
        .filter(el=>isPrime(Number(el))).length
}

function isPrime(number){
    if(number < 2){
        return false
    }
    for(let i=2; i*i<=number;i++){
        if(number % i === 0){
            return false
        }
    }
    return true
}