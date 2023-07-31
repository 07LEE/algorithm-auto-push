function solution(sides) {
    sides = sides.sort(function(a, b){
        return a - b;
    });
    if (sides[0] + sides[1] > sides[2]) {
        return 1;
    }else {
        return 2;
    }
}