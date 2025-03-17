def subarray_product_lesser_k(arr: list, k: int):
    current_product = 1
    total = 0
    left = 0
    for i in range(len(arr)):
        current_product *= arr[i]
        print(current_product)
        while left <= i and current_product >= k:
            current_product /= arr[left]
            left +=1

        print(f"left:{left}")
        total += i-left+1
    return total


if __name__ == '__main__':
    print(subarray_product_lesser_k([5, 7, 12], 10))
