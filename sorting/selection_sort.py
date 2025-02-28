
test1 = [3,1,9,5,11,7,3]
test2 = [1,3,5,7]
test3 = [1,1,1,1]
test4 = [7,3,2,1]

def selection_sort(input_: []) -> list:
    for i in range(0, len(input_) - 1):
        for j in range(i+1, len(input_)):
            if input_[i] >= input_[j]:
                _ = input_[i]
                input_[i] = input_[j]
                input_[j] = _


    print(input_)

if __name__ == '__main__':
    selection_sort([5, 8, 3, 9, 4, 1, 7])
    selection_sort(test2)
    selection_sort(test3)
    selection_sort(test4)

