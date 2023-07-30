function solution(s) {
    let answer = '';
    let list = s.split(" ");
    
    for (let i in list) {
        for (let j in list[i]){
            if (j % 2 == 0) {
                answer += list[i][j].toUpperCase();
            } else {
                answer += list[i][j].toLowerCase();
            };    
        };
        if (i != list.length - 1) {
                 answer += ' '
            };
    };
    
    return answer;
}