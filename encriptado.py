from bitarray import bitarray
import numpy as np
import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits):
    return binascii.unhexlify('%x' % int('0b'+bits, 2))

def string_to_list(string):
    bits = []
    inp = list(string)
    for i in inp:
        bits.append(int(i))
    return bits

def list_to_string(list):
    string = ''.join([str(i) for i in list])
    return string


def xor(a, b):
    a = list_to_string(a)
    b = list_to_string(b)
    y = int(a, 2)^int(b,2)
    x = bin(y)[2:].zfill(len(a))
    x = string_to_list(x)
    return x

def ip(inp):
    bits = []
    for i in  [2, 6, 3, 1, 4, 8, 5, 7]:
       bits.append(inp[i-1]) 
    return bits
def ipin(inp):
    bits = []
    for i in  [4, 1, 3, 5, 7, 2, 8, 6]:
       bits.append(inp[i-1]) 
    return bits
def expansion(inp):
    bits = []
    for i in  [4, 1, 2, 3, 2, 3, 4, 1]:
       bits.append(inp[i-1]) 
    return bits
def p10(inp):
    bits = []
    for i in  [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]:
       bits.append(inp[i-1]) 
    return bits
def ls1(inp):
    bits = []
    for i in  [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]:
       bits.append(inp[i-1]) 
    return bits
def p8(inp):
    bits = []
    for i in  [6, 3, 7, 4, 8, 5, 10, 9]:
       bits.append(inp[i-1]) 
    return bits
def p4(inp):
    bits = []
    for i in  [2, 4, 3, 1]:
       bits.append(inp[i-1]) 
    return bits
def mitad(lista):
    mitad = int((len(lista))/2)
    m1 = lista[:mitad]
    m2 = lista[mitad:]
    return(m1, m2)
def switch(lista):
    parte = mitad(lista)
    nuevo = parte[1] + parte[0]
    return nuevo
def ls1(inp):
    bits = []
    for i in  [2, 3, 4, 5, 1]:
       bits.append(inp[i-1]) 
    return bits
def ls2(inp):
    bits = []
    for i in  [3, 4, 5, 1, 2]:
       bits.append(inp[i-1]) 
    return bits
def sbox(a, b):
    a = list_to_string(a)
    b = list_to_string(b)
    s0 = {'0000': '01', '0010':'00', '0100':'11', '0110':'10',
    '0001':'11', '0011':'10', '0101':'01', '0111':'00',
    '1000':'00', '1010':'10', '1100':'01', '1110':'11',
    '1001':'00', '1011':'01', '1101':'11', '1111':'10'}

    s1 = {'0000': '00', '0010':'01', '0100':'10', '0110':'11',
    '0001':'10', '0011':'00', '0101':'01', '0111':'11',
    '1000':'11', '1010':'00', '1100':'01', '1110':'10',
    '1001':'10', '1011':'01', '1101':'00', '1111':'11'}
    sbox1 = string_to_list(s0[a])
    sbox2 = string_to_list(s1[b])

    return (sbox1, sbox2)

def llaves(llave):
    perm1 = p10(llave)
    mit1 = mitad(perm1)
    jun1 = ls1(mit1[0]) + ls1(mit1[1])
    mit2 = mitad(jun1)
    jun2 = ls2(mit2[0]) + ls2(mit2[1])
    k1 = p8(jun1)
    k2 = p8(jun2)
    return(k1, k2)

def ronda(m, k):
    m = mitad(m)
    exp = expansion(m[1])
    xo = xor(exp, k)
    parti = mitad(xo)
    sboxes = sbox(parti[0], parti[1])
    jun = sboxes[0] + sboxes[1]
    perm = p4(jun)
    res = xor(perm, m[0])
    lista = res + m[1]
    return lista

def encriptado(m, k):
    m = string_to_list(m)
    k = llaves(string_to_list(k))
    perm1 = ip(m)
    ronda1 = ronda(perm1, k[0])
    sw = switch(ronda1)
    ronda2 = ronda(sw, k[1])
    c = list_to_string(ipin(ronda2))

    return c

def desencriptado(c, k):
    c = string_to_list(c)
    k = llaves(string_to_list(k))
    perm1 = ip(c)
    ronda1 = ronda(perm1, k[1])
    sw = switch(ronda1)
    ronda2 = ronda(sw, k[0])
    m = list_to_string(ipin(ronda2))

    return m   
''' 
m = '10100101'
k = '0010010111'

c = (encriptado(m, k))
print(c)
j = (desencriptado(c, k))
print(j)
if m == j:
    print('si')
'''