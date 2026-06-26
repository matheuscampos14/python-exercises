def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def is_valid(state, col):
        row = len(state)
        for r, c in enumerate(state):
            if c == col:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True

    def dfs(state):
        if len(state) == n:
            solutions.append(state[:])
            return
        for col in range(n):
            if is_valid(state, col):
                state.append(col)
                dfs(state)
                state.pop()
    dfs([])
    return solutions

print(dfs_n_queens(4))