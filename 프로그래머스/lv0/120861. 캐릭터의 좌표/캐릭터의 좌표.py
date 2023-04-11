def solution(keyinput, board):
    max_x = int((board[0] - 1)//2)
    max_y = int((board[1] - 1)//2)
    x, y = 0, 0

    for i in keyinput:
        if i == 'left':
            if x > -(max_x):
                x -= 1
        elif i == 'right':
            if x < max_x:
                x += 1
        elif i == 'up':
            if y < max_y :
                y += 1
        elif i == 'down':
            if y > -(max_y) :
                y -= 1

    answer = [x, y]
    return answer