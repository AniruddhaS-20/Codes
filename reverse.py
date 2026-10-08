number=int(input("Enter a number: "))
num1=number
num2=0
while number>number:
    digit=number%10
    num2=num2*10+digit
    number//=10

print("The reverse of the number is:", num2)