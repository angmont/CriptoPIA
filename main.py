import encriptado
import base64
import os

def img_to_bits(path):
    with open(path, "rb") as lectura:
        encrip = base64.b64encode(lectura.read())
    nobytes = encrip.decode('UTF-8')
    men = encriptado.text_to_bits(nobytes)
    return men

def img_cif(nombre, ext, c):
    with open(nombre + ext, "w") as img:
        img.write(c)
        img.close()

def bits_to_img(nombre, ext, m):
    men1 = encriptado.text_from_bits(m)
    um = men1.decode('UTF-8')
    c = base64.b64decode(um)
    with open(nombre + ext, "wb") as img:
        img.write(c)
        img.close()

def first_read(nombre):
    with open(nombre, 'rb') as lectura:
        cosa = lectura.read()
    nobytes = cosa.decode('UTF-8', errors="ignore")
    try:
        men = encriptado.text_from_bits(nobytes)
        return True
    except:
        return False
def read_img(nombre):
    with open(nom, "r") as img:
        j = img.read()
        img.close()
    return j
def check_the_key(key):
    try:
        prueba = int(key)
        lon = len(key)
        if lon == 10:
            return True
        else:
            return False
    except:
        return False
    return j
def check_the_file(nom):
    try:
        with open (nom, "r") as img:
            img.close()
        name, extension = os.path.splitext(nom)
        return (name, extension)
    except:
        return False

if __name__ == "__main__":

    while True:
        dec = input('Cifrado[1]\nDescifrado[2]\n')
        c = ''
        m = ''
        if dec == '1':
            nom = input('Inserte el nombre de la imagen\n: ')
            check = check_the_file(nom)
            if check != False:
                nombre = check[0] + '_cif'
                ext = check[1]
                k = input('Inserte la llave:\n')
                prueba = check_the_key(k)
                if prueba == True:
                    x = first_read(nom)
                    if x == False:
                        men = img_to_bits(nom)
                        ko = men
                        nop = 1
                    else:
                        j = read_img(nom)
                        men = j
                        ko = men
                        nop = 2
                    
                    for i in range(int((len(men))/8)):
                        bits = ko[:8]
                        enc = encriptado.encriptado(bits, k)
                        ko = ko[8:]
                        c = c + enc
                        
                    if nop == 2:
                        try:
                            bits_to_img(nombre, ext, c)
                        except:
                            img_cif(nombre, ext, c)
                    else:
                        img_cif(nombre, ext, c)
                    print('Listo!\n')
                else:
                    print('La llave es incorrecta')
            else:
                print('Ingresó un path equivocado')
            
        elif dec == '2':
            nom = input('Inserte el nombre de la imagen\n: ')
            check = check_the_file(nom)
            if check != False:
                nombre = check[0] + '_des'
                ext = check[1]
                k = input('Inserte la llave:\n')
                prueba = check_the_key(k)
                if prueba == True:
                    bitsono = first_read(nom)
                    if bitsono == True:
                        j = read_img(nom)
                    else:
                        j = img_to_bits(nom)

                    for i in range(int((len(j))/8)):
                        bint = j[:8]
                        des = encriptado.desencriptado(bint, k)
                        j = j[8:]
                        m = m + des
                    try:
                        bits_to_img(nombre, ext, m)
                    except:
                        img_cif(nombre, ext, m)
                    print('Listo!')
                else:
                    print('La llave es incorrecta')
            else:
                print('Ingresó un path equivocado')                
        else: 
            print('Adios!')
            break

