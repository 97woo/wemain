def reverse(number):
      
#   if number >= 0:
#     return number[::-1]
  
  if number > 0:
    return int(str(number)[::-1])
  else:
    return -int(str(number).replace("-",'')[::-1])




print(reverse(-4321))