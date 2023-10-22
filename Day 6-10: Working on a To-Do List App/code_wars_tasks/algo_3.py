def multiples_of_3_or_5(number):
    if number < 0:
        return 0

    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum


result = multiples_of_3_or_5(10)
print(result)
