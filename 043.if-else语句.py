# 请用户输入一个年龄
age = input("请输入您的年龄：")
# 判断用户年龄是否大于18
if 18 <= int(age) and 30 >= int(age):
    print("您已经成年了！！")
elif 30 <= int(age) and  40>= int(age):
    print("有点大！！！")
else:
    print("您还未成年！！")

    
