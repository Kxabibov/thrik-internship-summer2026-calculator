from add import add

def multiply_by_add(a, b):
    result = 0

    for _ in range(b):
        result = add(result, a)

    return result