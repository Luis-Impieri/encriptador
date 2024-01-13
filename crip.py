import random
import string

digs = string.punctuation + string.digits + string.ascii_letters + ' '
digs = list(digs)
cript = digs.copy()

random.shuffle(cript)

original = input("Mensagem")
criptografado = ""

for letter in original:
    index = digs.index(letter)
    criptografado += cript[index]

print(criptografado)

op = int(input("Deseja desencriptar a mensagem? Escolha 1 para SIM e 2 para NAO"))

if op == 1:
    print(f"mensagem original: {original}")
elif op == 2:
    print("Caso deseja desencriptar no futuro, aqui estão os valores correspondentes: ")
    print(f"digitos originais: {digs}")
    print(f"digitos embaralhados: {cript}")
else:
    print("Opção não valida")