import encriptado
import base64

def img_to_bits(path):
    with open(path, "rb") as lectura:
        encrip = base64.b64encode(lectura.read())
    nobytes = encrip.decode('UTF-8')
    men = encriptado.text_to_bits(nobytes)
    return men

def img_cif(nombre, c):
    with open(nombre + '.jpg', "w") as img:
        img.write(c)
        img.close()

def bits_to_img(nombre, m):
    men1 = encriptado.text_from_bits(m)
    um = men1.decode('UTF-8')
    c = base64.b64decode(um)
    with open(nombre + '.jpg', "wb") as img:
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
if __name__ == "__main__":

    dec = input('Cifrado[1]\nDescifrado[2]\n')
    c = ''
    k = '0101010101'
    m = ''
    if dec == '1':
        nom = input('Inserte el nombre de la imagen\n: ')
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
        
        nom = 'img_cif'
        if nop == 2:
            bits_to_img(nom, c)
        else:
            img_cif(nom, c)
        
    elif dec == '2':
        nom = input('Inserte el nombre de la imagen\n: ')

        j = read_img(nom)

        for i in range(int((len(j))/8)):
            bint = j[:8]
            des = encriptado.desencriptado(bint, k)
            j = j[8:]
            m = m + des
        nomb = 'img_des'
        bits_to_img(nomb, m)

