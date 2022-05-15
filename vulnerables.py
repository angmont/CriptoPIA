import encriptado
with open('llaves.txt', 'r') as texto:
    lineas = texto.readlines()
    texto.close()
llaves = []
for i in lineas:
    llaves.append(i[:10])
with open('mensajes.txt', 'r') as texto:
    lineas = texto.readlines()
    texto.close()
mensajes = []

for i in lineas:
    mensajes.append(i[:8])

#VULNERABILIDAD 1
'''
print('Vulnerabilidad 1')
for i in llaves:
    cont = 0
    for j in mensajes:
        enc1 = encriptado.encriptado(j, i)
        enc2 = encriptado.encriptado(enc1, i)
        if enc2 == j:
            cont = cont + 1
    if cont == 256:
        print(i)
'''
print('Vulnerabilidad 2')
angela = llaves[:340]
dari = llaves[340:681]
ian = llaves [681:1024]

for i in llaves:
    for j in llaves:
        cont = 0
        for x in mensajes:
            enc1 = encriptado.encriptado(x, i)
            enc2 = encriptado.encriptado(enc1, j)
            if enc2 == x:
                cont = cont + 1
            if enc2 != x:
                break
        if cont == 256:
            print(i, j)


