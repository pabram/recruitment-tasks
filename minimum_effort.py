import sys


def minimum_effort(filename):
    """Main function calculating minimum effort for each of
    previously prepared matrices"""
    for matrix in prepare_file(filename):
        calculate(matrix)


def prepare_file(filename):
    """Opening file, and preparing it for further work
    - dividing into matrices consisting of integers"""
    prepared = []
    # transforming each line from string to integer
    with open(filename, "r") as infile:
        lines = [line.replace("\n", "").split(",") for line in infile]
        matrices = [[int(val) for val in line] for line in lines]

    # dividing file into single matrices
    startpoint = 0  # index of element containing n value
    while startpoint < len(matrices) - 1:
        n = matrices[startpoint][0]  # n for current matrix
        matrix = matrices[startpoint + 1:startpoint + n + 1]  # current matrix
        prepared.append(matrix)
        startpoint += n + 1  # n for next matrix
    return prepared


def calculate(matrix):
    """Calculating minimal effort for given matrix. For each field in top row
     minimum effort is sum of all fields to the left, same with first column.
     For [1][1] field minimum effort is its value + smaller value from either
     field above or field to the left."""
    # minimum(and only possible) effort for first row
    for i in range(1, len(matrix[0])):
        matrix[0][i] += matrix[0][i - 1]

    # minimum(and only possible) effort for first column
    for i in range(1, len(matrix)):
        matrix[i][0] += matrix[i - 1][0]

    # minimum effort for remaining fields
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[1])):
            matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])

    print(matrix[-1][-1])

if __name__ == "__main__":
    minimum_effort(sys.argv[1])
