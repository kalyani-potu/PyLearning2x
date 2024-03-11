vowels = ['a','e','i','o','u']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
str = input("Enter the string : ")
v_count = 0
c_count = 0
for i in str:
    if i in vowels:
        v_count = v_count+1
    else :
        c_count = c_count+1
print("No of vowels in the given string is : ", v_count)
print("No of consonants in the given string is : ", c_count)
