print("= = = 简易计算器 = = =")
num1 = float(input("输入第一个数字"))
num2 = float(input("输入第二个数字"))
operator = input("输入运算符")
if operator == "+":
    print(f"{num1}+{num2}={num1+num2}")
elif operator == "-":
    print(f"{num1}-{num2}={num1-num2}")
elif operator == "*":
    print(f"{num1}*{num2}={num1*num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1}/{num2}={num1/num2}")
    else:
        print("错误：除数不能为零")