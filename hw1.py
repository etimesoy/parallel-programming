from random import randrange
from time import perf_counter


def generate_random_matrix(size: int) -> [[int]]:
    return [[randrange(1, 1_000_000) for _ in range(size)] for _ in range(size)]


# 1) i j k
# 2) i k j
# 3) j i k
# 4) j k i
# 5) k i j
# 6) k j i
def multiply_method(matrix1: [[int]], matrix2: [[int]], n: int, method_number: int) -> [[int]]:
    result_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if method_number == 1:
                    result_matrix[i][j] += matrix1[i][k] + matrix2[k][j]
                elif method_number == 2:
                    result_matrix[i][k] += matrix1[i][j] + matrix2[j][k]
                elif method_number == 3:
                    result_matrix[j][i] += matrix1[j][k] + matrix2[k][i]
                elif method_number == 4:
                    result_matrix[j][k] += matrix1[j][i] + matrix2[i][k]
                elif method_number == 5:
                    result_matrix[k][i] += matrix1[k][j] + matrix2[j][i]
                else:
                    result_matrix[k][j] += matrix1[k][i] + matrix2[i][j]
    return result_matrix


def main():
    n = int(input("Введите N - размер матриц: "))
    matrix1 = generate_random_matrix(n)
    matrix2 = generate_random_matrix(n)
    for method_number in range(1, 7):
        start_time = perf_counter()
        for runs_count in range(10_000):
            matrix3 = multiply_method(matrix1, matrix2, n, method_number=1)
        end_time = perf_counter()
        diff_time = end_time - start_time
        print(f"Способ {method_number} занял {diff_time} секунд")


if __name__ == "__main__":
    main()
