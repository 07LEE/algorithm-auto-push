for _ in range(3):
    wt, wm, ws, lt, lm, ls = map(int, input().split())
    work_time = wt*3600 + wm* 60 + ws
    leave_time = lt*3600 + lm* 60 + ls
    times = leave_time - work_time
    print(f'{times//3600} {(times%3600)//60} {(times%3600)%60}')