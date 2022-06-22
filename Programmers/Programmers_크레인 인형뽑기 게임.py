def solution(board, moves):
    answer = 0
    stack = [0]
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if not stack:
                    stack.append(board[j][i-1])
                    continue
                new = board[j][i-1]
                if stack[-1] == new:
                    stack.pop()
                    cnt += 2
                    print(stack)
                else:
                    stack.append(new)
                board[j][i-1] = 0
                break
            
           
    return cnt