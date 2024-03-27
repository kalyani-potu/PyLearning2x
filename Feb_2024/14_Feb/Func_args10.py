def rev_str(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str

result = rev_str(input("Enter the string: "))
print(result)

##################### or ##########
or_str1 = "Kalyani"
rev_str2 = or_str1[::-1]
print(rev_str2)