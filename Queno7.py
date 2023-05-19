# Write a python script to add a finally block for the above script
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
finally:
  print('The finally block always run if there is exception or not')