def generate_all_subsets(ip: str):
    result = []
    subset:str = ""
    result = generate_helper(ip, result, subset)
    return result


def generate_helper(ip:str , result: list, subset:str):
    if ip == "":
        result.append(subset)
        # print(result)

    else:
        generate_helper(ip[1:], result, subset)
        generate_helper(ip[1:], result, subset + ip[0])
    return result

if __name__ == '__main__':
    print(generate_all_subsets("xyz"))

