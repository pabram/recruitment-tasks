def minimum_effort(filename):
    for each in prepare_file(filename):
        calculate(each)


def prepare_file(filename):
    prepared = []
    # transforming each line from string to integer
    with open(filename, "r") as infile:
        lines = [line.replace("\n", "").split(",") for line in infile]
        matrices = [[int(val) for val in line] for line in lines]

    # dividing file into single matrices
    startpoint = 0  # index of element containing n value - for first matrix it's first element
    while startpoint <= len(matrices) - 1:
        n = int(matrices[startpoint][0])  # n for current matrix
        matrix = matrices[startpoint + 1:startpoint + n + 1]  # current matrix
        startpoint += n + 1  # n for next matrix
        prepared.append(matrix)
    return prepared


def calculate(matrix):
    # minimum effort for first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # minimum effort for first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    # minimum effort for remaining fields
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[1])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    print(matrix[-1][-1])
