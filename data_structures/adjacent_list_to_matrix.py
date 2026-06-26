def adjacency_list_to_matrix(base):
    n = len(base)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in base:
        for j in base[i]:
            matrix[i][j] = 1

    for line in matrix:
        print(line)
    return matrix

adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
