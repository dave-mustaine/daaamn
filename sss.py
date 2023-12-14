def exchange_rows(matrix, vector, row1, row2):    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


vector[row1], vector[row2] = vector[row2], vector[row1]


def scale_row(matrix, vector, row, divisor):
    matrix[row] = [elem / divisor for elem in matrix[row]]
    vector[row] /= divisor


def blend_rows(matrix, vector, row, source_row, factor):
    matrix[row] = [(a + k * factor) for a, k in
    zip(matrix[row], matrix[source_row])]


vector[row] += vector[source_row] * factor


def solve(matrix, vector):
    for column in range(len(vector)):        pivot_row = max(range(column, len(matrix)),
                                                             key=lambda r: abs(matrix[r][column]))
    if pivot_row != column:
        exchange_rows(matrix, vector, pivot_row, column)
    scale_row(matrix, vector, column, matrix[column][column])
    for r in range(column + 1, len(matrix)):            blend_rows(matrix, vector, r, column, -matrix[r][column])


solution = [0] * len(vector)
for i in range(len(vector) - 1, -1, -1):        solution[i] = vector[i] - sum(
    x * a for x, a in zip(solution[(i + 1):], matrix[i][(i + 1):]))
return solution

my_matrix = [[1, 0, 0, -1, -1, 0], [0, -1, 1, 1, 0, 0],
             [-1, 1, 0, 0, 0, -1], [-2, -4, 0, -3, 0, 0],
             [0, 4, 5, 0, 0, 4], [0, 0, -5, 3, -3, 0]]
my_constants = [0, 0, 0, -16, 18, -10]
print(solve(my_matrix, my_constants))
