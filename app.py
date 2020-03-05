#hello
from binarytree import Node, build
import numpy as np 

n1 = int(input('Ingres el tamaño de la lista 1:  '))
n2 = int(input('Ingres el tamaño de la lista 2:  '))

l1 = np.random.randint(low=1,high=100, size=n1)
l2 = np.random.randint(low=1,high=100, size=n2)

tree = build(np.sort(l1))
print(tree) 
