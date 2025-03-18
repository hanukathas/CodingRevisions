def card_points(arr, k):
    min_sum = sum(arr[:k])
    running_sum = min_sum
    for i in range(k, len(arr)):
        running_sum += arr[i] - arr[i - k]
        print(min_sum, running_sum)
        min_sum = min(running_sum, min_sum)
    return sum(arr) - min_sum


if __name__ == '__main__':
    print(card_points([1, 4, 3, 5, 9, 11, 3], 3))
