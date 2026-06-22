def subtractProductAndSum(n: int) -> int:
    product = 1
    sum_ = 0

    # last = n % 10
    rem = n

    for i in range(n):
        last = rem % 10

        product *= last
        sum_ += last

        rem = rem // 10

    print(product, sum_)
    return product - sum_

subtractProductAndSum(234)