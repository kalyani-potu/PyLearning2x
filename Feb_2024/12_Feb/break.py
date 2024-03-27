for counter in range(11) :
    if counter == 5:
        break
    print(counter)
print("outside the loop1")

for counter in range(11) :
     if counter == 5:
        continue
     print(counter)
print("outside the loop2")

for counter in range(11) :
     if counter == 5:
        pass
     print(counter)
print("outside the loop3")

for counter in range(11) :
     print(counter)
     if counter == 5:
        pass
print("outside the loop4")