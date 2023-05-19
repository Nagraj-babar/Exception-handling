# Write a python script to implement try except and else block for division
try:
    a=int(input('Enter a first value: '))
    b=int(input('Enter a secound value: '))
    if b==0:
     raise ZeroDivisionError
except ZeroDivisionError:
  print('You enterd zero')
else:
  print(a/b)
