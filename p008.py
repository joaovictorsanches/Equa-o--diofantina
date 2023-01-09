#Criador: João Victor Sanches Andrade
from random import randint
from os import system
system('clear')
a = None
num = int(input('Numero: '))
while a != num:
	system('clear')
	y = randint(0, num + 10)
	x = randint(0, num + 10)
	z = randint(0, num + 10)
	a = (x**3) + (y ** 3) + (z**3)
	print(a)
system('clear')

print(x, y, z)
print(a)
