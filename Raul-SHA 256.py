import hashlib
#print (hashlib.algorithms_guaranteed)
#print (hashlib.algorithms_available)
#
#
#


#print('##### CHECKING #####')
#cadena = str() #returns an empy string
#print('cadena set to nill:',cadena,'. Lenght', len(cadena))
#cadena = input('Input value :')
#print('cadena is now:',cadena,'. Length', len(cadena))
#print('##### END #####')

print('##### CODE START #####')
while True: # This constructs an infinite loop
    cadena = input(' Cadena que vamos a hashear: ')
    cadena_b = cadena.encode('utf-8')
    print('STR   :',cadena)
    print('BYTE  :',cadena_b)                         
    h = hashlib.sha256()
    h.update(cadena_b)

    jaseo = h.hexdigest()
    print('HASH       :',jaseo)
    print('digest_size:',h.digest_size)
    print('blck_size  :',h.block_size)

   
    
print('##### CODE FINISH #####')
