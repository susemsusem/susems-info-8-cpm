def susem(numbers):
    summ = 0
    q = 0
    for i in numbers:
        summ += int(i)
        q+= 1
    if q == 0:
        print('Вы не ввели ни одного числа')
    else:
        return summ/q
numbers = 1, 2, 3, 4
print(susem(numbers))