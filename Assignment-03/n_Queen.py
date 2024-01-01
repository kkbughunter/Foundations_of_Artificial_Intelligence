def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]
    
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N):
    # Base case: If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column, return False
    return False


def solve_n_queens(N):
    # Initialize the board with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False

    # Print the solution
    print("Solution for", N, "queens:")
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    return True


# Example usage:
n = 4  # Change the value of n to solve for different board sizes
solve_n_queens(n)
