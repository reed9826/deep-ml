def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == "row":
        for i in range(len(matrix)):
            temp = 0
            for j in range(len(matrix[i])):
                temp += matrix[i][j]
            n = temp/len(matrix[i])
            means.append(n)
    elif mode == "column":
         for i in range(len(matrix[0])):
            temp = 0
            for j in range(len(matrix)):
               temp += matrix[j][i]
            n = temp/len(matrix)
            means.append(n)    

    return means