def insertionSort(arr):
    comp = 0
    for i in range(1, len(arr)):
        newElem = arr[i]
        j = i - 1
        while j >= 0 and newElem < arr[j]:
            comp += 1
            arr[j + 1] = arr[j]
            j -= 1
        else:
            if j >= 0:
                comp += 1
        arr[j + 1] = newElem
    return comp


with open('input.txt', 'r') as file:
    arr = [int(num) for num in file.readline().split()]
comp = insertionSort(arr)
with open('output.txt', 'w') as file:
    file.write('{}\n{}'.format(' '.join(map(str, arr)), comp))
