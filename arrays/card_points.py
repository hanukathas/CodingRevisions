def card_points(arr, k):
    min_sum = sum(arr[:k])
    running_sum = min_sum
    for i in range(k, len(arr)):
        running_sum += arr[i] - arr[i - k]
        print(min_sum, running_sum)
        min_sum = min(running_sum, min_sum)
    return sum(arr) - min_sum

def card_points_revision(arr, k):
    n = len(arr)

    cur_sum = sum(arr[:k])
    max_sum = cur_sum
    for i in range(k):
        # print(arr[i])
        cur_sum = cur_sum + arr[i] - arr[n - k + 1]
        max_sum = max(max_sum, cur_sum)
    return max_sum



if __name__ == '__main__':
    # print(card_points([1,2,3,4,5,6,1], 3))
    print(card_points_revision([1, 2, 3, 4, 5, 6, 1], 3))
