for num in range(1,10):
    if num % 2 == 0:
        print(f'found even number {num}')
        continue
    print(f'odd number {num}')
print("-----------------------------------")

for num in range(1,10):
    if num % 2 == 0:
        print(f'found even number {num}')
        pass
    print(f'odd number {num}')