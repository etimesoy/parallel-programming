from random import randrange
from time import perf_counter


def generate_random_matrix(size: int) -> [[float]]:
    return [[1_000_000_000.0 for _ in range(size)] for _ in range(size)]


# 1) i j k
# 2) i k j
# 3) j i k
# 4) j k i
# 5) k i j
# 6) k j i
def multiply_method(matrix1: [[float]], matrix2: [[float]], n: int, method_number: int) -> [[float]]:
    result_matrix = [[0 for _ in range(n)] for _ in range(n)]
    if method_number == 1:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    elif method_number == 2:
        for i in range(n):
            for k in range(n):
                for j in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    elif method_number == 3:
        for j in range(n):
            for i in range(n):
                for k in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    elif method_number == 4:
        for j in range(n):
            for k in range(n):
                for i in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    elif method_number == 5:
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    else:
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix


def main():
    n = int(input("Введите N - размер матриц: "))
    matrix1 = generate_random_matrix(n)
    matrix2 = generate_random_matrix(n)
    for method_number in range(1, 7):
        start_time = perf_counter()
        matrix3 = multiply_method(matrix1, matrix2, n, method_number=1)
        end_time = perf_counter()
        diff_time = end_time - start_time
        print(f"Способ {method_number} занял {diff_time} секунд")


if __name__ == "__main__":
    main()
