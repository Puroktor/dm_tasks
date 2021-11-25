def partition(arr, i, j):
    pivot = arr[i]
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def select_part(arr, k):
    left = 0
    right = len(arr) - 1
    while True:
        v = partition(arr, left, right)
        if k < v:
            right = v - 1
        elif k > v:
            left = v + 1
        else:
            return k


def insertion_sort(arr, start, stop):
    for i in range(start + 1, stop + 1):
        elem = arr[i]
        j = i - 1
        while j >= start and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem


def select_opt(arr, k, left, right):
    w = 5
    while True:
        d = right - left + 1
        if d <= w:
            insertion_sort(arr, left, right)
            return left + k
        dd = d // w

        for i in range(dd):
            insertion_sort(arr, left + i * w, left + (i + 1) * w - 1)
            m = left + i * w + ceil_div(w, 2) - 1
            arr[left + i], arr[m] = arr[m], arr[left + i]

        v = select_opt(arr, ceil_div(dd, 2), left, left + dd - 1)
        arr[left], arr[v] = arr[v], arr[left]
        v = partition(arr, left, right)
        temp = v - left + 1

        if k < temp:
            right = v - 1
        elif k > temp:
            k -= temp
            left = v + 1
        else:
            return v


def ceil_div(a, b):
    return -(a // -b)


def main():
    with open('input.txt', 'r') as file:
        k = int(file.readline())
        arr = list(map(int, file.readline().split()))
    i1 = select_part(arr, k)
    elem1 = arr[i1]
    i2 = select_opt(arr, k, 0, len(arr) - 1)
    elem2 = arr[i2]
    with open('output.txt', 'w') as file:
        file.write(str(elem1))
        file.write('\n')
        file.write(str(elem2))


if __name__ == '__main__':
    main()
