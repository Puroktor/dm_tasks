import math


def insertion_sort(arr, start, incr):
    comp = 0
    for i in range(start + incr, len(arr), incr):
        elem = arr[i]
        j = i - incr
        while j >= start and elem < arr[j]:
            comp += 1
            arr[j + incr] = arr[j]
            j -= incr
        else:
            if j >= start:
                comp += 1
        arr[j + incr] = elem
    return comp


def shell_sort(arr, mode):
    comp = 0
    if mode:
        passes = math.floor(math.log2(len(arr)))
        increment = 2 ** passes - 1
    else:
        passes = math.floor(math.log(2 * len(arr) + 1, 3)) - 1
        increment = (3 ** passes - 1) // 2
    while passes >= 0:
        for start in range(0, increment):
            comp += insertion_sort(arr, start, increment)
        if mode:
            increment = (increment - 1) // 2
        else:
            increment = (increment - 1) // 3
        passes -= 1
    return comp


def main():
    with open('z5/input10.txt', 'r') as file:
        arr = list(map(int, file.readline().split()))
    comp1 = shell_sort(arr.copy(), True)
    comp2 = shell_sort(arr, False)
    with open('z5/output10.txt', 'w') as file:
        file.write('{}\n{} {}'.format(' '.join(map(str, arr)), comp1, comp2))


if __name__ == '__main__':
    main()
