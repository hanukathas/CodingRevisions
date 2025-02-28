test1 = [5, 2, 4, 6, 1, 3]
test2 = [1,1,1,1]
test3 = [2,2,2,2]
test4 = []


def segregate_even_off(numbers: []) -> []:
    i = 0
    j = len(numbers) - 1
    while i < j:
        print(i, j)
        if numbers[i] % 2 == 0 and numbers[j] % 2 == 1:
            i += 1
            j -= 1
        elif numbers[i] % 2 == 0 and numbers[j] % 2 == 0:
            i += 1
        elif numbers[i] % 2 == 1 and numbers[j] % 2 == 1:
            j -= 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
    return numbers

if __name__ == '__main__':
    print(segregate_even_off(test1))
    print(segregate_even_off(test2))
    print(segregate_even_off(test3))
    print(segregate_even_off(test4))