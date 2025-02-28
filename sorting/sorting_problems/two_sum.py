sum = 14
arr = [1,5,10,4,9,11,12,1]

def merge_sort(arr: []) -> []:
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right) -> []:
    final_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final_arr.append(left[i])

            i += 1
        else:
            final_arr.append(right[j])

            j += 1
    while i < len(left):
        final_arr.append(left[i])

        i += 1

    while j < len(right):
        final_arr.append(right[j])

        j += 1
    return final_arr

def two_pointer(arr, sum) -> int:
    left = 0
    right = len(arr) -1
    match_count = 0

    while left < right:

        if arr[left] + arr[right] == sum:
            match_count += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] < sum:
            left += 1
        else:
            right -= 1
    return match_count

if __name__ == '__main__':
    sorted_arr = merge_sort(arr=arr)
    print(sorted_arr)
    print(two_pointer(sorted_arr, 14))