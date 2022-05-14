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

for i in llaves:
    cont = 0
    for j in mensajes:
        enc1 = encriptado.encriptado(j, i)
        enc2 = encriptado.encriptado(enc1, i)
        if enc2 == j:
            cont = cont + 1
    if cont == 256:
        print(i)


