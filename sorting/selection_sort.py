def selection_sort(numbers):
    for i in range(len(numbers)):
        smallest = numbers[i]
        for j in range(i+1, len(numbers)):
            if smallest > numbers[j]:
                numbers[i] = numbers[j]
                numbers[j] = smallest
                smallest = numbers[i]
    return numbers

print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))