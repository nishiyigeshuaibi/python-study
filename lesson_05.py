# price = int(input("请输入商品价格："))
#
# if price >= 30:
#     print("免运费")

price = int(input("请输入商品价格："))

# if price >= 30:
#     shipping_fee = 0
# else:
#     shipping_fee = 6

if price >= 30:
    shipping_fee = 0
elif price >= 20:
    shipping_fee = 3
else:
    shipping_fee = 6

print("总价", price + shipping_fee)
