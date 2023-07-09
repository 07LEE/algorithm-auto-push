def solution(price, money, count):
    return sum([price*i for i in range(1, count+1)]) - money if sum([price*i for i in range(1, count+1)]) > money else 0