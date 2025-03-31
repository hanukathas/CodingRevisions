def stock_max_profit(arr: list):
    least_value_index = 0
    max_profit = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[least_value_index]:
            least_value_index = i
            continue
        elif arr[i] > arr[least_value_index]:
            max_profit = max(max_profit, arr[i] - arr[least_value_index])

    return max_profit

def stock_max_profit_revision(arr: list):
    max_profit = 0
    least_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[least_index]:
            max_profit = max(max_profit, arr[i] - arr[least_index])
        else:
            least_index = i
            continue
    return max_profit


if __name__ == '__main__':
    print(stock_max_profit([7,6,4,3,1]))
    print(stock_max_profit_revision([7,1,5,3,6,4]))