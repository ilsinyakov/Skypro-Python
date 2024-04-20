def bank(x, y):
    sum = x
    for _ in range(y):
        sum += sum * 0.1
    return sum

print(bank(100, 2))
