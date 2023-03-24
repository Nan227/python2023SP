def total(values):
  t=0
  for x in value:
    t = t + x
  return t

def is_even1(values):
  
  return[x %2 ==0 for x in values]
#res[] # someting will go wrong
def is_even2(values):
  res = []
  print(f"DBG: init res ={res}")
  for x in values:
    res.append(x % 2 == 0)
    #res = res +[ x% 2 ==0 => error]
  return res

def is_even3(values):
  res =[None] * len(values)
  for i in range(len(values)):
    res[i] = values[i]% 2 ==0
    print(f"DBG: iter end res={res} i ={i}")
  return res

def sqtotal(values):
  t = 0
  for x in values:
    t = t + x**2
  return t

def any_even(values):
  res= False
  print(f"DBG: init res ={res}")
  for x in values:
    x_even = x%2 ==0
    if x_even:
      res = True
      return res
  return res


def any_even2(values):
  for x in values:
    x_even = x%2 ==0
    if x_even:
      return True
  return False