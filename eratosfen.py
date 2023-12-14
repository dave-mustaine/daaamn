numbers = [i for i in range(2, int(input()) + 1)]
length = len(numbers)
for i in range(length):
    if numbers[i]:
        number = numbers[i]
        k = i + number
        while k <= length - 1:
            numbers[k] = 0
            k += number

print(*(x for x in numbers if x))
