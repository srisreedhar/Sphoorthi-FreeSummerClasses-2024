# collect 2 values from users
# compare these 2 values and print which one is greater

num1 = input("Enter any number, num1: ")
num2 = input("Enter another number, num2 : ")


num1 = int(num1)
num2 = int(num2)


if num1 > num2:
    print("num1 ",num1," is GREATER than ",num2)
elif num1 < num2:
    print("num1 ",num1," is LESSER than ",num2)
elif num1 == num2:
    print("num1 ",num1," is EQUAL to",num2)
else:
    print("I cannot evaluate")
    
    
