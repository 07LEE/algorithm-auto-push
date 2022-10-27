def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr3 = [arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))]
        answer.append(arr3)
    return answer