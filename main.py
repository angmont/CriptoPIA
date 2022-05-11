import encriptado
import base64
from PIL import Image


if __name__ == "__main__":

    dec = input('Cifrado[1]\nDescifrado[2]\n')
    if dec == '1':
        c = ''
        k = '0010010111'
        m = ''
        with open('minion.jpg', "rb") as img_file:
	        b64_string = base64.b64encode(img_file.read())

        test_str = b64_string.decode('UTF-8')
        men = encriptado.text_to_bits(test_str)
        ko = men
        for i in range(int((len(men))/8)):
            bits = ko[:8]
            enc = encriptado.encriptado(bits, k)
            ko = ko[8:]
            c = c + enc
        for i in range(int((len(c))/8)):
            bint = c[:8]
            des = encriptado.desencriptado(bint, k)
            c = c[8:]
            m = m + des

        #ko = text_from_bits(m)
        men1 = encriptado.text_from_bits(m)
        with open("img_desencriptada.bin", 'w') as img:
            img.write(men1.decode('UTF-8'))
            img.close()

        file = open('img_desencriptada.bin', 'rb')
        byte = file.read()
        file.close()

        decodeit = open('img_desencriptada.jpg', 'wb')
        decodeit.write(base64.b64decode((byte)))
        decodeit.close()  
'''    
        print('o')

        escritura = open("Gilmore.txt", "w")
        for i in range(int((len(c))/8)):
            bint = men[:8]
            escritura.write(bint + '\n')
            men =  men[8:]
        escritura = open("Gilmore2.txt", "w")
        for i in range(int((len(c))/8)):
            bint = m[:8]
            escritura.write(bint + '\n')
            m =  m[8:]
        # reading files
        f1 = open("Gilmore.txt", "r")
        f2 = open("Gilmore2.txt", "r")

        i = 0
        x = 0
        for line1 in f1:
            i += 1
            
            for line2 in f2:
                
                # matching line1 from both files
                if line1 == line2:
                    # print IDENTICAL if similar
                    pass	
                else:

                    print("Line ", i, ":")
                    # else print that line from both files
                    print("\tFile 1:", line1, end='')
                    print("\tFile 2:", line2, end='')
                    x = x + 1
                break
        print ('lineas: ', i)
        # closing files
        f1.close()									
        f2.close()	
        if x == 0:
            print('sin diferencias')	
        print('end')
        print(len(test_str))	
        print(len(m))	
        print(len(men))	
        print(type(men))
        print(type(m))	
        first_set = set(men)
        second_set = set(m)
        difference = first_set.symmetric_difference(second_set)

        print(difference)
        if m == men:
            print('igual')
        else:
            print('error')			

        #ko = text_from_bits(m)
        men1 = encriptado.text_from_bits(m)
        with open("img_desencriptada.bin", 'w') as img:
            img.write(men1.decode('UTF-8'))
            img.close()

        file = open('img_desencriptada.bin', 'rb')
        byte = file.read()
        file.close()

        decodeit = open('img_desencriptada.jpg', 'wb')
        decodeit.write(base64.b64decode((byte)))
        decodeit.close()       
'''
