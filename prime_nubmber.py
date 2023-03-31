def prime_number(values):
  res=False
  print(f"DEB: init res= {res}")
  for x in values:
    if x ==2:
      res = True
      print(f"DEB: init_end res= {res} [x= {x}]")
    elif x==3:
      res = True
      print(f"DEB: init_end res= {res} [x= {x}]")
    else:
      res = False
      print(f"DEB: init_end res= {res} [x= {x}]")
      return False
      
      print(f"DEB: init_end res= {res} [x= {x}]")
  return res