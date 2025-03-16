def circle_sort(arr: list):
    processed_index = []
    for i in range(len(arr)):
        if len(processed_index) == len(arr):
            break
        if i in processed_index:
            continue
        else:
            processed_index.append(i)
        right_place = False
        while not right_place:
            lesser_numbers_count = 0
            for j in range(i, len(arr)):
                if arr[i] > arr[j]:
                    lesser_numbers_count +=1
            if lesser_numbers_count == 0:
                right_place = True
            else:
                right_place = False
                arr[i], arr[i+lesser_numbers_count] = arr[i+lesser_numbers_count], arr[i]
                processed_index.append(i+lesser_numbers_count)
        print(arr)
    return arr

if __name__ == '__main__':
    print(circle_sort([8,9,6,3,0,2,7,5,4,1,10]))



