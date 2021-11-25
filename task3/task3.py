from math import floor
def linearSearch(arr, elem):
    comp=0
    for a in arr:
        comp+=1
        if a == elem:
            break
    return comp

def binarySearch(arr, elem):
    comp, start, end = 0, 0, len(arr)-1
    while start <= end:
        middle = (start + end)//2
        comp+=1
        if arr[middle] == elem:
            break
        elif arr[middle] < elem:
            start = middle + 1
        else:
            end = middle - 1
    return comp

def interpolSearch(arr, elem):
    comp, left, right = 0, 0,len(arr)-1
    while left <= right:
        ind = left + floor((right-left)/(arr[right]-arr[left])*(elem-arr[left]))
        comp+=1
        if arr[ind] == elem:
            break
        elif arr[ind] < elem:
            left = ind + 1
        else:
            right = end - 1
    return comp

def countAvComp(arr, func):
    comp = 0
    for i in range(1, len(arr)+1):
        comp += func(arr, i)
    return comp/len(arr)

with open('input.txt', 'r') as file:
    arr = [int(num) for num in file.readline().split()]
    
linComp=countAvComp(arr, linearSearch)
binComp=countAvComp(arr, binarySearch)
intComp=countAvComp(arr, interpolSearch)

with open('output.txt', 'w') as file:
    file.write('{}\n{}\n{}'.format(linComp, binComp, intComp))
