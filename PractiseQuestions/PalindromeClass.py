class Palindrome():
    def palindrome_check(self,str):
        str1 = ''
        for i in str:
            str1 = i + str1
        return str1

palindrome_ref = Palindrome()
str_input = input("Enter the string:").lower()
if palindrome_ref.palindrome_check(str_input) == str_input:
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")

