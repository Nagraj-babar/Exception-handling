# Write a python script to raise a ValueError.
try:
    a=int(input('Enterd a value: '))
    if a==0:
        raise ValueError
except ValueError:
    print('It raise value error')
finally:
    print('if you enterd zero then it will raise valuerror')