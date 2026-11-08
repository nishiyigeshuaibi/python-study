# coins = 3
#
# while coins > 0:
#     print("剩余金币", coins)
#     coins -= 1
#
# print("金币用完了")
#
# products = []
#
# while True:
#     product = input("请输入商品名，输入 q 结束：")
#     if product == "q":
#         break
#     if product == "" or product == "测试":
#         continue
#     products.append(product)
#
# print(products)

# scores = [55, 60, 75, 90]
#
# for score in scores:
#     if score < 60 or score >= 90:
#         print(score)


def is_passing(score):
    return score >= 60


def count_passing(scores):
    count = 0

    for score in scores:
        if is_passing(score):
            count += 1
    return count


print("及格人数", count_passing([55, 60, 75, 90]))

