def solution(price, money, count):
    total_price = 0
    for i in range(count):
        total_price += price*(i+1)

    return total_price-money if money < total_price else 0