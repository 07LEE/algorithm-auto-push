function solution(n) {
    let answer = 0;
    let num = n.toString().split('')
    for (let i in num){
        answer += Number(num[i])
    }
    
    return answer;
}