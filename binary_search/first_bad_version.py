def is_bad_version(version_id: int):
    return version_id >= 4

def first_bad_version(max_version: int):
    start = 1
    end = max_version

    while start <= end:
        mid = start + (end -  start) // 2

        if is_bad_version(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start

if __name__ == '__main__':
    print(first_bad_version(20))

