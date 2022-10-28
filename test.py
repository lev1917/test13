


def my_exp(x, n =100):
    current = 1
    exp_x = 1
    for k in range(1,n+1):
        current *= x/k
        exp_x+=current
    return exp_x


print(my_exp(3))


