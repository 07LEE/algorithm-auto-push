function solution(money) {
    let cnt = 0;
    for (let i = 5500; money >= i ; money = money - i) {
        cnt ++;
    }
    let answer = [cnt, money];
    return answer;
}