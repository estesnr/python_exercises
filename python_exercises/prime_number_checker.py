def prime_checker(number):
  is_prime = True
  for x in range(2, number):
    if number % x == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number")
  else:
    print("Not a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)
