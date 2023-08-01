function solution(todo_list, finished) {
    var answer = [];
    for (let i = 0; i < todo_list.length; i ++) {
        if (finished[i] == 0) {
            answer.push(todo_list[i])
        }
    }
    return answer;
}