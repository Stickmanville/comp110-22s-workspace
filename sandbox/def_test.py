def sub(numbers: list[int], start: int, end: int) -> list[int]:
    """Given a list, spits out a subset of the list."""
    new_list: list[int] = []
    i: int = start
    if i < 0:
        i = 0
    if end > len(numbers):
        true_end = len(numbers) - 1
    else:
        true_end: int = end - 1
    while i <= true_end:
        number: int = numbers[i]
        new_list.append(number)
        i += 1
    return new_list
    

a_list: list[int] = [10, 20, 30, 40]
print(sub(a_list, 0, 6))