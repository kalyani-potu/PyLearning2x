str1 = input("Enter the first string : ").lower()
str2 = input("Enter thee second string : ").lower()
list1 = list(str1)
list2 = list(str2)
list1.sort()
list2.sort()
print(list1)
print(list2)
if list1 == list2:
    print("Given strings are anagrams")
else:
    print("Given strings are not anagrams")

#################### or ############
sorted_str1 = sorted(str1) #sorted function returns sorted list.
print(sorted_str1)
sorted_str2 = sorted(str2)
print(sorted_str2)
if sorted_str1 == sorted_str2:
    print("Given strings are anagrams")
else:
    print("Given strings are not anagrams")
