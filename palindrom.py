number=int(input("Enter a number: "))
org_num=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number//=10
    

if reverse==org_num:
    print("The number is a palindrome.")
    print("The reverse of the number is:", reverse)
else:
    print("The number is not a palindrome.")
    print("The reverse of the number is:", reverse)