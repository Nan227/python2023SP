def prime_number(n):
  for x in range(2, n):
    res = False
    if x ==2:
      res = True
      print(f"DEB: init_end res= {res} [x= {x}]")
    elif x==3:
      res = True
      print(f"DEB: init_end res= {res} [x= {x}]")
    elif x==5:
      res = True
      print(f"DEB: init_end res= {res} [x= {x}]")
    elif x==7:
      res = True
      print(f"DEB: init_end res= {res} [x= {x}]")
    elif x>=8:
      if (x%2==0) and (x%3==0) and (x%5==0) and(x%7==0):
        res = True
        print(f"DEB: init_end res= {res} [x= {x}]")
    else:
      res = False
      print(f"DEB: init_end res= {res} [x= {x}]")
      return False
      
      print(f"DEB: init_end res= {res} [x= {x}]")
  return res

#print(prime_number(50))

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
  print(f"DBG: out of loop")
  return True

print("Is prime number " )
print( prime_number2(3))
print("Is prime number" + str(prime_number3(9)))
def dic():
  for n in address_of.item():
    print(x)
    