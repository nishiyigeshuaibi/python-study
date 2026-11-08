def show_greeting():
    print("欢迎学习 Python")


def show_price(price):
    print("价格", price)


def add_coins(coins):
    return coins + 5


def calculate_shipping(price):
    if price >= 30:
        shipping_fee = 0
    elif price >= 20:
        shipping_fee = 3
    else:
        shipping_fee = 6
    return shipping_fee


def calculate_total(price, shipping_fee):
    return price + shipping_fee


def calculate_sum(prices):
    total = 0
    for price in prices:
        total += price
    return total


show_greeting()

show_price(18)
show_price(30)

total_coins = add_coins(20)
print("金币", total_coins)

print(calculate_shipping(19))
print(calculate_shipping(20))
print(calculate_shipping(30))

price = int(input("请输入商品的价格："))
shipping_fee = calculate_shipping(price)
total = calculate_total(price, shipping_fee)
print("总价", total)

total = calculate_sum([18, 32, 25])
print("合计", total)

print(calculate_sum([]))
print(calculate_sum([8]))