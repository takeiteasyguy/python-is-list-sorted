def compare_values(v1, v2):
    try:
        if v1 > v2:
            return "NO"
    except TypeError:
        return "ERROR"


def is_sorted_while(l):
    i = 1
    while i < len(l):
        res = compare_values(l[i-1], l[i])
        if res:
            return res
        i += 1
    return "YES"


def is_sorted_for(l):
    for i in range(1, len(l)):
        res = compare_values(l[i - 1], l[i])
        if res:
            return res
    return "YES"


def is_sorted_internal_sorted_func(l):
    try:
        really_sorted = sorted(l)
    except TypeError:
        return "ERROR"
    if really_sorted == l:
        return "YES"
    else:
        return "NO"


def is_sorted_list_sorted_method(l):
    try:
        really_sorted = list(l)
        really_sorted.sort()
    except TypeError:
        return "ERROR"
    if really_sorted == l:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    l_sorted = [1, 2, 8, 11]
    l_unsorted = [1, 5, 8, 10, 3]
    l_error = [1, 2, 5, 8, "some string", 4, 2]

    assert is_sorted_while(l_sorted) == "YES"
    assert is_sorted_while(l_unsorted) == "NO"
    assert is_sorted_while(l_error) == "ERROR"

    assert is_sorted_for(l_sorted) == "YES"
    assert is_sorted_for(l_unsorted) == "NO"
    assert is_sorted_for(l_error) == "ERROR"

    assert is_sorted_internal_sorted_func(l_sorted) == "YES"
    assert is_sorted_internal_sorted_func(l_unsorted) == "NO"
    assert is_sorted_internal_sorted_func(l_error) == "ERROR"

    assert is_sorted_list_sorted_method(l_sorted) == "YES"
    assert is_sorted_list_sorted_method(l_unsorted) == "NO"
    assert is_sorted_list_sorted_method(l_error) == "ERROR"

    print("Done, everything is OK")
