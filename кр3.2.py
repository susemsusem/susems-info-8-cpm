inpt = [228, 8800, 777, 888, 1007]
def count(n):
    d = 0
    while n > 0:
        d += n % 10
        n //= 10
    return d
def searching(inpt):
    var = 0
    ans = []
    for number in inpt:
        summ = count(number)
        if summ > var:
            var = summ
            ans = [number]
        elif summ == var:
            ans.append(number)
    return ans

result = searching(inpt)

print(result)