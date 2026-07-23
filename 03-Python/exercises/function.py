def calculator(num1, num2, operator):
    if operator == "+" :
        return f"{num1}+{num2}={num1+num2}"
    elif operator == "-" :
        return f"{num1}-{num2}={num1-num2}"
    elif operator == "*" :
        return f"{num1}*{num2}={num1*num2}"
    elif operator == "/" :
        if num2 != 0 :
            return f"{num1}/{num2}={num1/num2}"
        else :
            return "错误：除数不能为零"
    else :
        return "未知运算符，不在此计算机能力之内"
print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))
print(calculator(10, 0, "/"))
print(calculator(10, 5, "^"))
