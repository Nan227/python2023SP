#next week : 1, is_even :out 2 all even 3 any_even?


#input[5,2,1,3] Output [False, True,False,False]

# def is_even(values):
#  # t=values[0] 
#   for i in range(len(values)):
#     if values[i] % 2 == 0:
#       values[i]=True
#       # print(values[i])
#     else:
#       values[i]=False
#       # print(values[i])
#   return values[i]

#[x%]

def is_even(values):
  res = [] 
  #print("result" + res)
 # t=values[0] 
  for x in values:
    res.append(x%2 == 0)
  return res


def is_even2(values):
  return [x %2 ==0 for x in values]

  #range(len(values)):
  #   result[i] =(values[i] % 2 ==0)
  #   print(f"result{result} i =[i]")
  # return result
  #   #if values[i] % 2 == 0:
  #     values[i]=True
  #     # print(values[i])
  #   else:
  #     values[i]=False
  #     # print(values[i])
  # return values[i]
test = [1,3,8,7]
print(test)
print(is_even(test))

#---------Check all even ?----------

def all_even(values):
  for num in values:
    # checking condition
    if num % 2 != 0:
       return False
  return True
  
print("Is all even number?")
if (all_even(test)):
  print("Yes, all number is even")
else:
  print("No, there are at least one of them is odd number")

#-------Check all odd ?------------

def all_odd(values): 
  for num in values:
    # checking condition
    if num % 2 == 0:
       return False
  return True

print("Is all odd number?")

if (all_odd(test)):
  print("YEs, all number is odd number")
else:
  print("No, at least one of them is even number")