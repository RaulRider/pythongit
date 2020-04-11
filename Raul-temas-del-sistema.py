import sys

#imprimir lista de PATH
#sys.path tiene toda la infromacion de directorios
for i in range(len(sys.path)):
   print(sys.path[i])



#imprimir lista NOMBRES definidos en un MODULO 
lista_nombres = dir(sys)
num_nombres = len(lista_nombres)
print('Numero de Nombres en el modulo: ', num_nombres)
for i in range(0, num_nombres):
    print(lista_nombres[i], '\n')
    

#imprimir lista de MODULOS
# sys.modules es el diccionario de modulos
# por ejemplo poner >>> 'numpy' in sys.modules te devuelve
# True si está en los modulos y False si no está

num_mod = len(list(sys.modules.keys())) 
lista_modulos = list(sys.modules.keys())
print('Numero de Modulos: ', num_mod)
for i in range(0, num_mod, 20):
    print(lista_modulos[i], '\n', sys.modules[lista_modulos[i]], '\n')
    print('...')
    

