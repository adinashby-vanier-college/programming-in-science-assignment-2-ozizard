def max_two_in_list(numbers):

    max_val = scond_max = None

    for num in numbers:
        if max_val is None or num > max_val:
            second_max, max_val = max_val, num
        elif num != max_val and (second_max is None or num > second_max):
            second_max = num
    return max_val, second_max

def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))

def cumulative_sum(arr):
    result = [ ]
    total = 0

    for num in arr:
        total += num
        result.append(total)

    return result

def transpose_matrix(matrix):
    return [list(row) for row in zip (*matrix)]

def slice_every_nth(lst, step):
    return lst[::step]

def dot_product(list1, list2):
    return sum(a * b for a, b in zip(list1, list2))

def matrix_multiplication(matrix1, matrix2):
    rows_A, cols_A = len(matrix1), len(matrix1[0])
    rows_B, cols_B = len(matrix2), len(matrix2[0])

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result