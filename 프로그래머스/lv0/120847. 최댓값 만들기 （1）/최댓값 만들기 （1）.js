function solution(numbers) {
    numbers = numbers.map(Number);
    numbers.sort(function(a, b)  {return a - b;})
    return numbers[numbers.length-1] * numbers[numbers.length-2]
}