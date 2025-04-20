def smallest_letter_greater_than_target(arr: list, target: str):
    start = 0
    n = len(arr)
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] > target:
            end = mid - 1
        else:
            start = start + 1

    return  arr[start % n]

if __name__ == '__main__':
    print(smallest_letter_greater_than_target(['c', 'f', 'j'], 'a'))
    print(smallest_letter_greater_than_target(['c', 'f', 'j'], 'c'))
    print(smallest_letter_greater_than_target(['c', 'f', 'j'], 'd'))
    print(smallest_letter_greater_than_target(['c', 'f', 'j'], 'k'))