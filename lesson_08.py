product_prices = {"苹果": 18, "香蕉": 32, "橙子": 26}

product_prices["香蕉"] = 30
product_prices["葡萄"] = 28

# print(product_prices)

total = 0

for product, price in product_prices.items():
    if price >= 28:
        total += price

print("合计", total)