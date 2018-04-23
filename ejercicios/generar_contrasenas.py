import random

caracteres = "abcdefghijklmnospqrstuvwxyzABCDEFGHIJKLMNOSPQRSTUVWXYZ1234567890$#@"

numero, longitud = input("Número Longitud ").split()

numero = int(numero)
longitud = int(longitud)

arreglo_password = []

for i in range(numero):
    password = "".join(random.sample(caracteres, longitud))

    if password in arreglo_password:
        pass
    else:
        arreglo_password.append(password)

print(arreglo_password)
text_file = open("pass.txt", "w")
text_file.write("\n".join(arreglo_password))
text_file.close()
