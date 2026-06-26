def verify_card_number(numbers):
    numbers = numbers.replace(' ', '').replace('-', '')
    digits = numbers[::-1]
    total = 0
    for i, digit in enumerate(digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
        if n > 9:
            n -= 9
        total += n
    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'

print(verify_card_number('4111-1111-1111-1111'))