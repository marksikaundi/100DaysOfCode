def multiples_of_3_or_5(number):
    if number < 0:
        return 0

    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum


def test_multiples_of_3_or_5():
    assert multiples_of_3_or_5(0) == 0
    assert multiples_of_3_or_5(1) == 0
    assert multiples_of_3_or_5(2) == 0
    assert multiples_of_3_or_5(3) == 0
    assert multiples_of_3_or_5(4) == 3
    assert multiples_of_3_or_5(5) == 3
    assert multiples_of_3_or_5(6) == 8
    assert multiples_of_3_or_5(7) == 14
    assert multiples_of_3_or_5(8) == 14
    assert multiples_of_3_or_5(9) == 14
    assert multiples_of_3_or_5(10) == 23


if __name__ == '__main__':
    test_multiples_of_3_or_5()
    print('All tests passed')






