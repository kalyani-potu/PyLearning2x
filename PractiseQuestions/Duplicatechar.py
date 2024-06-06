#removing duplicate chararcters
str = input("Enter the input string :")
str1 = ''
for i in str:
    if i in str1:
        continue
    else:
        str1 = str1 + i
print(str1)