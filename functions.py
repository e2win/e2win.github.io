def factorial(num, type="int"):
    answer = 1
    for i in range(1, num+1):
        answer *= i
    if type == "stg":
        return "Word version of your number is : " + str(answer) + " "
    else:
        return answer

print(factorial(12, "stg"))
print(factorial(4))