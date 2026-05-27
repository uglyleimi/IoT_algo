def find_last_occurrence(haystack, needle):
    if not needle or not haystack:
        return -1, 0

    comparisons = 0
    last_index = -1

    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break

        if match:
            last_index = i + len(needle) - 1

    return last_index, comparisons


haystack = "hello world, hello everyone"
needle = "hello"
result_index, comp_count = find_last_occurrence(haystack, needle)
print(f"Кінцевий індекс: {result_index}")
print(f"Кількість порівнянь: {comp_count}")
