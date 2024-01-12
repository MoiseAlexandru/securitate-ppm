import hashlib
from Crypto.Cipher import AES
#from Cryptodome.Util.Padding import pad
#from Cryptodome.Random import get_random_bytes

cipher = AES.new("cheie", AES.MODE_ECB)

def cripteaza_litera(litera):
    path = "./litere-ppm/" + litera + ".ppm"
    print(path)
    with open(path, 'r', encoding='ANSI') as fisier:
        p6 = fisier.readline().strip()
        dim = fisier.readline().split(" ")
        size_x, size_y = dim[0].strip(), dim[1].strip()
        pixel = fisier.readline()

        imagine = fisier.readlines()

        header = p6 + " " + size_x + " " + size_y + " " + pixel
        encrypted_header = hashlib.sha256(header.encode('UTF-8'))
        imagine_criptata = cipher.encrypt(imagine)

        print(imagine_criptata)




cripteaza_litera('S')