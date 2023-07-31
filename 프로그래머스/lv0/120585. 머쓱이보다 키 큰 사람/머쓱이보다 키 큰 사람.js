function solution(array, height) {
    var answer = 0;
    for (let i in array) {
        if (array[i] > height) {
            answer ++;
        }
    }
    return answer;
}