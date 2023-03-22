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
test = [2, 4, 7 ,8]
print(is_even(test))
#print(is_even2(test))

def all_even(values): 
  res = [] 
  
  for x in values:
    res.append(x%2 == 0)
  #return res
    for i in range(len(res)):
     
      if i==False:
        result= False
        print(result)
      else:
        result = True
        print(result)
      return res
  #print(res)

print(all_even(test))

# def all_odd(res): 
#   for i in res:
#     if i==False:
#       result= True
#     else:
#       result = False
#   return result
# print(f"All numers are {result} the odd numbers")