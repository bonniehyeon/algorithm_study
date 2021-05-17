def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


if __name__ == "__main__":
    print('Test case is running.....')
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    n = 10
    target = 7
    print(f'Array is {array} with size {n}.')
    print(f'Now, we are looking for where {target} is')
    target_idx = binary_search(array, target, 0, n - 1)
    print(f'{target}\'s index is {target_idx}')

'''
***output***

Test case is running.....
Array is [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] with size 10.
Now, we are looking for where 7 is
7's index is 3
'''
