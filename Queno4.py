# Write a python script to handle a ValueError
try:
 a,b=[1,2,3] # critical statement
except ValueError:
 print('In list there are three element but you enterd two variable for it ')
