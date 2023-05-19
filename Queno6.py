'''Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions.'''
try:
 a=int(input('Enter a first number: '))
 b=int(input('Enter a secound number:  '))
 c=input('enter a operant: e.g +,-,*,/ :  ')
 if c in"+,-*,/":
  if c=="+":
    print(a+b)
  elif c=='-':
    print(a-b)
  elif c=='*':
    print(a*b)
  elif c=="/":
    print(a/b)
 else:
   raise ArithmeticError
except ValueError:
   print('You not give a value or enterd inapropreate data')
except ArithmeticError:
   print('You Enterd wroung operant')
except NameError:
   print('You not give a sufficent data ')
except Exception:
   print('You doing something wroung')