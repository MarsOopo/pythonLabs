#-*- config:utf-8 -*-

age=25
name='Caroline'

print('{0} is {1} years old.'.format(name,age))
print('{0} is a girl'.format(name))
print('{0:.3} is a decimal.'.format(1/3))
print('{0:_^11} is a 11 length'.format(name))
print('{first} is as {second}'.format(first=name,second='Wendy'))
print('My name is {0.name}'.format(open('out.txt','w')))
print('My name is {0:8}'.format('Fred'))

