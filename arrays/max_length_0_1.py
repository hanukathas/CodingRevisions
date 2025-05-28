def max_length_0_1(nums: list):
    hmap = {0: -1}  #empty sub array
    global_max = 0  #get the length
    excess = 0  #for 1, add an excess and for a 0, subtract excess. so excess = 0 for 1,0
    for i in range(len(nums)):
        if nums[i] == 1:
            excess += 1
        else:
            excess -= 1
        if excess in hmap:
            global_max = max(global_max, i + 1 - hmap[excess])
        if excess in hmap:
            hmap[excess] += i
        else:
            hmap[excess] = 1
    return global_max

def max_length_0_1_r(nums: list):
    hmap = {0:0}
    max_size = 0
    excess = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            excess += 1
        else:
            excess -= 1
        if excess in hmap:
            pass
        if excess in hmap:
            max_size = max(max_size, i  - hmap[excess])
        if excess in hmap:
            hmap[excess] += i
        else:
            hmap[excess] = 1
    return max_size

def max_length_r2(nums: list):
    hmap = {}
    excess = 1 if nums[0] == 0 else -1
    hmap[excess] = 0
    print(f"excess:{excess}")
    max_val = 0
    for i in range(1, len(nums)):
        if nums[i] == 0:
            excess += 1
        else:
            excess -= 1
        print(f"excess:{excess}")
        if excess in hmap:
            max_val = max(max_val, i + 1 - hmap[excess])
        hmap[excess] = i
        print(hmap)
    return max_val

if __name__ == '__main__':
    print(max_length_r2([0, 1, 1, 0, 1, 1, 0]))
    # print(max_length_0_1([0, 1]))
    # print(max_length_0_1([0, 1, 0]))
    # print(max_length_0_1([0, 1, 1, 1]))
    # print(max_length_0_1([0, 1, 1, 1, 0]))

    # print(max_length_r2([0, 1]))
    # print(max_length_r2([0, 1, 0]))
    # print(max_length_r2([0, 1, 0, 1]))

