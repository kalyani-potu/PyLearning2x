def palindrome(str1):
    str2 = ""
    n = len(str1) - 1
    for i in range(len(str1)):
        str2 = str2 + str1[n - i]
    if str2 == str1:
        print(f"{str1} is a palindrome")
    else:
        print(f"{str1} is not a palindrome")


input_str = input("Enter the string:")
palindrome(input_str)
