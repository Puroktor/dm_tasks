import math


def quick_sort(arr, first, last):
    comp = 0
    if first < last:
        pivot, comp = partition(arr, first, last)
        comp += quick_sort(arr, first, pivot)
        comp += quick_sort(arr, pivot + 1, last)
    return comp


# Разбиение Хоара
def partition(arr, i, j):
    comp = 0
    pivot = arr[i]
    while True:
        while arr[i] < pivot:
            comp += 1
            i += 1
        while arr[j] > pivot:
            comp += 1
            j -= 1
        if i >= j:
            return j, comp
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def generate_permutations(n):
    matrix = [[0 for x in range(n)] for y in range(math.factorial(n))]
    array = [x for x in range(1, n + 1)]
    permute(matrix, 0, array, 0)
    return matrix


def permute(matrix, to, arr, i):
    if i == len(arr):
        matrix[to] = arr.copy()
        to += 1
    else:
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            to = permute(matrix, to, arr, i + 1)
            arr[i], arr[j] = arr[j], arr[i]
    return to


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline())
    permutations = generate_permutations(n)
    max_comp = max_index = 0
    for k in range(math.factorial(n)):
        comp = quick_sort(permutations[k].copy(), 0, n - 1)
        if comp > max_comp:
            max_comp = comp
            max_index = k
    with open('output.txt', 'w') as file:
        file.write(str(permutations[max_index]))


if __name__ == '__main__':
    main()
