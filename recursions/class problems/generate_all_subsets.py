def generate_all_subsets(s: str):
    result = []
    slate = ""
    s = "".join(sorted(s))

    result = generator(s, result, slate)

    return result


def generator(s, result: list, slate: str):
    if s == "":
        result.append(slate)
    else:
        generator(s[1:], result, slate)
        generator(s[1:], result, slate + s[0])

    return list(set(result))


def generator_revision(s, result: list, slate: str):
    if s == "":
        result.append(slate)
    else:

        generator(s[1:], result, slate)
        generator(s[1:], result, slate + s[0])
    return list(set(result))





if __name__ == '__main__':
    print(generate_all_subsets("aab"))
