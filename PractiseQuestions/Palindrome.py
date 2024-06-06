str = input("Enter the string:").lower()
str1 = ''
for i in str:
    str1 = i + str1
if str1 == str:
    print("Given string is a palindrome")
else :
    print("Given string is not a palindrome")
