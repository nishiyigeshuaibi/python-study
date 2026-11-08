# # name = "  小 明  "
# # clean_name = name.strip()
# #
# # print(f"姓名：[{clean_name}]")
#
#
# def read_name():
#     while True:
#         name = input("请输入姓名：").strip()
#
#         if name == "":
#             print("姓名不能为空")
#         else:
#             return name
#
#
#
# name = read_name()
# print(f"姓名：[{name}]")

# while True:
#     command = input("请输入命令，输入 q 退出：").strip().lower()
#     if command == "":
#         continue
#     if command == "q":
#         break
#     elif command in ["help", "list"]:
#         print("命令有效")
#     else:
#         print("未知命令")


def mentions_python(text):
    return "python" in text.lower()


def parse_products(text):
    products = []
    text = text.replace("，", ",")
    for fruit in text.split(","):
        fruit = fruit.strip()
        if fruit:
            products.append(fruit)
    return products


# text = "苹果   香蕉"
# products = text.split()
# print(products)
#
# text = "苹果,,香蕉"
# print(text.split(","))

# print(parse_products(" 苹果，香蕉, ,橙子 "))

text = input("请输入商品：")
products = parse_products(text)
if products:
    print(f"商品：{'、'.join(products)}")
else:
    print("暂无商品")
