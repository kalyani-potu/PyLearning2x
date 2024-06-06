def palindrome(str1):
    str2 = ""
    for i in str1: # i refers to the charachters in string
        str2 = i + str2
    if str2 == str1:
        print(f"{str1} is a palindrome")
    else:
        print(f"{str1} is not a palindrome")


str = input("Enter the string:")
in_str = str.lower()
palindrome(in_str)

# using string index
'''
def palindrome(str1):
    str2 = ""
    n= len(str1)-1
    for i in range(len(str1)):
        str2 = str2 + str1[n-i]
    if str2 == str1 :
        print(f"{str1} is a palindrome")
    else :
        print(f"{str1} is not a palindrome")


str = input("Enter the string :")
in_str = str.lower()
palindrome(in_str)
'''