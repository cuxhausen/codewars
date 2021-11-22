
# Kata #1 Create Phone Number

"""Description:
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!"""

# My solutions
def create_phone_number(n):
    n.insert(0, '(')
    n.insert(4, ') ')
    n.insert(-4, '-')
    a = ""
    for i in n:
        a += str(i)
    return a

# Other solutions

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

def create_phone_number(n):
    str1 =  ''.join(str(x) for x in n[0:3])
    str2 =  ''.join(str(x) for x in n[3:6])
    str3 =  ''.join(str(x) for x in n[6:10])
    return '({}) {}-{}'.format(str1, str2, str3)

def create_phone_number(n):
    n = "".join([str(x) for x in n] )
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))

def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"

def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)

create_phone_number = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

def create_phone_number(n):
  d='('
  #for loop to go through the array
  for i in range(len(n)):
  #get the first part of the final string
      if i<3:
          d=d+str(n[i])
          if i==2:
              d=d+') '
  #get the middle part of the final string
      elif i>=3 and i<6:
         
          d=d+str(n[i])
          if i==5:
              d=d+'-'
  #get the last 4 string members of the final string
      elif i>=6 and i<10:
   
          d=d+str(n[i])
  # return the entire string        
  return d
