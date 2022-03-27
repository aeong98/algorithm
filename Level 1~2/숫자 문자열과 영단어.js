function solution(s) {
    let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    var answer = s;

    for(let i=0; i< numbers.length; i++) {
        // 해당 문자열을 기준으로 양옆으로 남은 문자열이 arr 배열에 들어감.
        let arr = answer.split(numbers[i]);
        // join 을 통해서 arr 배열을 다시 합쳐주면 arr 배열 원소들 사이에 i 가 들어가면서 새로운 문자열 생성
        answer = arr.join(i);
    }
    return Number(answer);
}