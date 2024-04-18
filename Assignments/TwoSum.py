sum_value = int(input("Enter the sum value :"))
list1 = [1,3,9,0,5,3,6]
c=1
for i in list1 :
    result = sum_value - i
    for n in range(c,len(list1)):
        if result == list1[n] :
            print(list1.index(i),n)
    c+=1
