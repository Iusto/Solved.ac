def count_max_candies(board):
    max_candies = 0
    # 가로 연속 사탕 개수 세기
    for row in board:
        count = 1
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                count += 1
            else:
                max_candies = max(max_candies, count)
                count = 1
        max_candies = max(max_candies, count)
    
    # 세로 연속 사탕 개수 세기
    for col in range(len(board[0])):
        count = 1
        for row in range(1, len(board)):
            if board[row][col] == board[row - 1][col]:
                count += 1
            else:
                max_candies = max(max_candies, count)
                count = 1
        max_candies = max(max_candies, count)
    
    return max_candies

def solve(board):
    n = len(board)
    max_candies = 0
    
    # 모든 인접한 칸을 교환하며 최대 연속 사탕 계산
    for i in range(n):
        for j in range(n):
            # 오른쪽과 교환
            if j + 1 < n:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                max_candies = max(max_candies, count_max_candies(board))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
            # 아래쪽과 교환
            if i + 1 < n:
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                max_candies = max(max_candies, count_max_candies(board))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
    
    return max_candies

# 예시 입력 받기
n = int(input())
board = [list(input()) for _ in range(n)]
print(solve(board))
