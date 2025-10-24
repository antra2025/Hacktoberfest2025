# Loop through numbers from 2 to 100
for num in range(2, 101):
   is_prime = True # Assume the number is prime
   # Check divisors from 2 to the square root of the number
   for divisor in range(2, int(num ** 0.5) + 1):
       if num % divisor == 0:
           is_prime = False # Not a prime number
           break
   if is_prime:
       print(num, end=", ")
