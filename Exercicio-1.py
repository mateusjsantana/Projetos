from random import choice
sorteio= (input('O sorteador irá lhe mostrar um número aleatório de 1 a 10, pressione Enter'))
lista=[1,2,3,4,5,6,7,8,9,10]
sorteado= choice(lista)
print('O numero sorteado foi: {}'.format(sorteado))

