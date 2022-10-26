def solution(numbers):
    numbers = sorted(numbers)
    return numbers[0] * numbers[1] if numbers[0] * numbers[1] > numbers[-1] * numbers[-2] else numbers[-1] * numbers[-2]