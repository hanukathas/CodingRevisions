def majority_element(arr: list):
    hmap = dict()
    for i in range(len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            if len(hmap) == 0:
                hmap[arr[i]] = 1
            else:
                key = list(hmap.keys())[0]
                hmap[key] -= 1
                if hmap[key] == 0:
                    hmap.pop(key)

    return list(hmap.keys())[0]

def majority_element_revision(arr: list):
    hmap = {}
    for i in range(len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            if len(hmap) == 0:
                hmap[arr[i]] = 1
            else:
                key = list(hmap.keys())[0]
                hmap[key] -= 1
                if hmap[key] == 0:
                    hmap.pop(key)
    return list(hmap.keys())[0]


if __name__ == '__main__':
    print(majority_element([1,1,1,0,7,0,5,5,5,5,5,5,5]))
    print(majority_element_revision([1, 1, 1, 0, 7, 0, 5, 5, 5, 5, 5, 5, 5]))

