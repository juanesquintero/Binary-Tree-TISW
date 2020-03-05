#hello
from binarytree import Node, bst, build
import numpy as np 

n1 = int(input('Ingres el tamaño de la lista 1:  '))
n2 = int(input('Ingres el tamaño de la lista 2:  '))

l1 = np.random.randint(low=1,high=100, size=n1)
l2 = np.random.randint(low=1,high=100, size=n2)

lista = np.concatenate((l1,l2), axis=None)


tree = build(np.sort(l1)[::-1])
tree2 = build(np.sort(l2)[::-1])

tree3 = build(np.sort(lista)[::-1])

print('lista 1: ', l1, 'lista 2: ', l2, 'Arbol 1: ', tree, 'Arbol 1: ', tree2, 'Lista Unificada: ',lista,'Arbol Unificado: ', tree3 )

