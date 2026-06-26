def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[-1]
    print(pivot)

    less = []
    equal = []
    greater = []

    for num in numbers:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([4, 42, 16, 23, 15, 8]))