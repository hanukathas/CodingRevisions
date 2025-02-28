test1 = [3,1,9,5,11,7,3]
test2 = [1,3,5,7]
test3 = [1,1,1,1]
test4 = [7,3,2,1]

def insertion_sort(input_: []) -> []:
    for i in range(0, len(input_)):
        temp = input_[i]
        red = i - 1
        while red >= 0 and input_[red] > temp:
            input_[red+1] = input_[red]
            red -= 1
            print(input_)
        input_[red+1] = temp

    return input_


if __name__ == '__main__':
    print(insertion_sort([5, 8, 3, 9, 4, 1, 7]))
    # print(insertion_sort([]))
    # print(insertion_sort(test2))
    # print(insertion_sort(test3))
    # print(insertion_sort(test4))