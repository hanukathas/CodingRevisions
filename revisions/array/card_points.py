def card_points(arr, k):
    """
    calculate the min sum of k cards from the array
    :param arr:
    :param k:
    :return:
    """
    # check base conditions
    prefix = sum(arr[:k])
    min_sum = prefix

    for i in range(k, len(arr)):
        prefix = prefix - arr[i-k] + arr[i]
        min_sum = min(prefix, min_sum)

    return sum(arr) - min_sum

if __name__ == '__main__':
    print(card_points([1,2,3,4,5,6,1], 3))
