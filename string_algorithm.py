def getSubString(n):
  """This is simple logic for getting max substring in a string 
     whose sum of first and second half should be equal and the
     sub string should be of maximum length

     condition: String should have integers only
     """
  if len(n)%2 == 0:
    iter_num = len(n)
  else:
    iter_num = len(n) - 1
  while iter_num > 0:
    for i in range(len(n)):
      if i + iter_num > len(n):
        break
      else:
        temp1 = n[i: i + iter_num]
        iter_mid = iter_num/2
        first = temp1[0: iter_mid]
        second = temp1[iter_mid: iter_num]
        if returnSumOfStringIntegers(first) == returnSumOfStringIntegers(second):
          return iter_num, temp1
    iter_num -= 2
  return 0

def returnSumOfStringIntegers(sub_sub_string):
  """This wil return the sum of all the integers in the passed string"""
  sum_string_integers = 0
  for i in  [int(j) for j in str(sub_sub_string)]:
    sum_string_integers += i
  return sum_string_integers

print getSubString("986561517416921217551395112859219257312")
