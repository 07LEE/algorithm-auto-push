def solution(ineq, eq, n, m):
    if eq == '=':
        if eval(f'{n} {ineq}{eq} {m}') is True:
            return 1
        else:
            return 0
    else :
        if eval(f'{m} {ineq} {n}') is True:
            return 0
        else:
            return 1