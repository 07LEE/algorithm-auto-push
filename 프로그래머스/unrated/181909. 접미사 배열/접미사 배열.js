function solution(my_string) {
    var answer = [];
    for (let i = 0; i < my_string.length ; i++ ) {
        answer.push(my_string.slice(i, my_string.length))
    }
    answer.sort()
    return answer;
}