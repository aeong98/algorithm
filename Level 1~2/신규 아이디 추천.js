function solution(new_id) {
    var answer = new_id
        // 모두 소문자로 치환
        .toLowerCase()
        // 알파벳 소문자, 숫자, 빼기, 마침표를 제외한 모든 문자 제거
        .replace(/[^\w-_.]/g, '')
        // . 이 2번 이상 연속된 부분은 하나의 마침표 (.) 로 치환
        .replace(/\.{2,}/g, '.')
        // (.) 이 처음이나 끝에 위치한다면 제거
        .replace(/^\.|\.$/g, '')
        // 빈 문자열이면 "a" 를 대입
        .replace(/^$/, 'a')
        // 16자 이상이면 이후의 문자 제거
        .slice(0, 15).replace(/\.$/, '');
    
    const len= answer.length;
    // new_id 의 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복한다.
    return len > 2 ? answer : answer + answer.charAt(len-1).repeat(3-len);
    
    return answer;
}