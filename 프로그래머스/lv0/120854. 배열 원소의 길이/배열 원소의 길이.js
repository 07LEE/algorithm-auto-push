function solution(strlist) {
    var answer = [];
    for (let i in strlist) {
        answer.push(strlist[i].split("").length);
    };
    return answer;
}