class PrimeCheck:
    def prime_no_checker(self, num):
        if num <=1 :
            return False
        for i in range(2,(num//2+1)):
            if num % i == 0 :
                return False
        return True


prime_num = PrimeCheck()
n = int(input("Enter the number : "))
if prime_num.prime_no_checker(n):
    print("Given number is a prime number")
else :
    print("Given number is not a prime number")