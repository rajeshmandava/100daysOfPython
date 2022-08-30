def prime_checker(num):
  is_prime = True
  for i in range(2,num):
    if(num % i ==0):
      is_prime = False
  if is_prime:
    print(f"{num} is prime number")
  else:
    print(f"{num} is not  a primt number")





num = int(input("Enter a number for prime check:"))
prime_checker(num)