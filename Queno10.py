# Write a python script to implemented a nested Try Except block
try:
    try:
      a,b=[1,2,3]   
    except ValueError:
        print('You Enterd 2 variable excepted 3')
except Exception:
    print('An error occurs')
