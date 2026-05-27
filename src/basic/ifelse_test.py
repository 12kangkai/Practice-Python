# Python 分支判断示例

# 1. 简单的 if 判断
x = 10
if x > 5:
    print("x 大于 5")

# 2. if-else 判断
y = 3
if y % 2 == 0:
    print("y 是偶数")
else:
    print("y 是奇数")

# 3. if-elif-else 多分支判断
score = 78
if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 4. 嵌套 if 判断
z = 0
if z >= 0:
    print("z 是非负数")
    if z == 0:
        print("z 等于 0")
    else:
        print("z 是正数")
else:
    print("z 是负数")

# 5. 判断变量的真假:x=0、''、[]、()、None等都被认为是False，其他值都被认为是True。
x = 0
if x:
    print("x 是 True")
else:
    print("x 是 False")

x = ''
if x:
    print("x 是 True")
else:
    print("x 是 False")

x = []
if x:
    print("x 是 True")
else:
    print("x 是 False")

x = ()
if x:
    print("x 是 True")
else:
    print("x 是 False")

x = None
if x:
    print("x 是 True")
else:
    print("x 是 False")

# 6. 通过input输入判断
# age = int(input("请输入年龄: "))
# if age >= 18:
#     print("你是成年人")
# else:
#     print("你是未成年人")

# 7. 身高1.75，体重80.5kg。计算BMI（体重除以身高的平方）指数，并根据BMI指数,用if-elif判断并打印结果：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# height = 1.75
# weight = 80.5
# bmi = weight / (height ** 2)
# print(f"BMI指数: {bmi:.2f}")
# if bmi < 18.5:
#     print("过轻")
# elif bmi < 25:
#     print("正常")
# elif bmi < 28:
#     print("过重")
# elif bmi < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")


