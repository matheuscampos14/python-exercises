def dfs(matrix, label):
    if label < 0 or label >= len(matrix):
        print(f'Label deve ser entre 0 e {len(matrix)-1}')
        return -1

    result = []
    stack = [label]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for col in range(len(matrix[node])):
            if matrix[node][col] == 1 and col not in visited:
                stack.append(col)
    return result

matriz = [[0,1,1,0,0,0,0],
          [1,0,0,1,1,0,0],
          [1,0,0,0,0,1,1],
          [0,1,0,0,0,0,0],
          [0,1,0,0,0,0,0],
          [0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0]
          ]
print(dfs(matriz,0))


