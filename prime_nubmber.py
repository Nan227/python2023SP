

def prime_number2(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
      
      if n % i == 0:
          print(n)
          return False
    return True

def prime_number3(n):
  for d in range(2,n):
    print(f"DBG: iter start d {d}")
    if n %d ==0:
      return False
  #print(f"DBG: out of loop")
    return True

print("Is prime number " )
print( prime_number2(13))
print(f"Is prime number prime_number2: {prime_number2(9)}")


print(f"Is prime number, prime_number3:  {prime_number3(13)}")

print(f"Is prime number, prime_number3: {prime_number3(31)}")
