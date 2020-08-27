#This is my first Calculator
print("Enter the first number")
input1 = input()
print("Enter the second number")
input2 = input()
print("Enter the operation (+,-,*,/)")
input3 = input()
if input3 == "+":
    print(int(input1)+int(input2))
elif input3 == "-":
    print(int(input1)-int(input2))
elif input3 == "*":
    print(int(input1)*int(input2))
elif input3 == "/":
    print(int(input1)/int(input2))