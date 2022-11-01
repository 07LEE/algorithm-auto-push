def solution(n):
    ans = [0, 1]
    for i in range(2, n+1):
        ans.append(ans[i-2] + ans[i-1])
    
    return ans[-1]%1234567