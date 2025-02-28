test1 = [3,1,9,5,11,7,3]
test2 = [1,3,5,7]
test3 = [1,1,1,1]
test4 = [7,3,2,1]

def bubble_sort(input_: []) -> list:
    for i in range(0, len(input_) - 1):
        print(i)
        swap = False
        for j in range(len(input_) - 1, i, -1):
            if input_[j-1] >= input_[j]:
                swap = True
                _ = input_[j-1]
                input_[j - 1] = input_[j]
                input_[j] = _
            print(input_)
        if not swap:
            break
    return input_


if __name__ == '__main__':
    print(bubble_sort([5, 8, 3, 9, 4, 1, 7]))
    # print(bubble_sort([]))
    # print(bubble_sort(test1))
    # print(bubble_sort(test2))
    # print(bubble_sort(test3))
    # print(bubble_sort(test4))

