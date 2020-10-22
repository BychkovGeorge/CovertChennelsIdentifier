def print_matrix(matrix):
    for i in range(len(matrix[0])):
        string = ""
        for j in range(len(matrix[0])):
            string += str(matrix[i][j]) + " "
        print(string)

