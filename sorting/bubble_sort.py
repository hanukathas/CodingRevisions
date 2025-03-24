test1 = [3,1,9,5,11,7,3]
test2 = [1,3,5,7]
test3 = [1,1,1,1]
test4 = [7,3,2,1]

def bubble_sort(arr: []) -> list:
    for i in range(0, len(arr) - 1):

        swap = False
        for j in range(len(arr) - 1, i, -1):
            if arr[j-1] >= arr[j]:
                swap = True
                arr[j-1], arr[j] = arr[j], arr[j-1]
        if not swap:
            break
    return arr

def bubble_sort_revision(arr: []) -> list:
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr), i, -1):
            if arr[j-1] >= arr[j]:
                swap = True
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        if not swap:
            break
    return arr




if __name__ == '__main__':
    print(bubble_sort([5, 8, 3, 9, 4, 1, 7]))
    # print(bubble_sort([]))
    # print(bubble_sort(test1))
    # print(bubble_sort(test2))
    # print(bubble_sort(test3))
    # print(bubble_sort(test4))

