user_input = input("두 수를 입력하시오(공백으로 구분) : ")
num1, num2 = map(int, user_input.split())

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)