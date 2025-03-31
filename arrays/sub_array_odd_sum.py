def sub_array_odd_sum(arr: list) -> int:
    prefix_sum = 0
    # empty array is even sum, so when we start, event = 1, odd = 0
    hmap = {'even': 1, 'odd': 0}
    total = 0
    for i in range(len(arr)):
        prefix_sum = prefix_sum + arr[i]
        if prefix_sum % 2 == 0:
            total += hmap['odd']
        else:
            total += hmap['even']
        print(hmap, total)
        if prefix_sum % 2 != 0:
            hmap['odd'] += 1
        else:
            hmap['even'] += 1


    return  total

if __name__ == '__main__':
    print(sub_array_odd_sum([1,3,5]))