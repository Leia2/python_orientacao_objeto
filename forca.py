#Jogo da adivinhação

print("*************************************************************************")
print("**************** Bem vindo ao jogo da Forca!*****************************")
print("*************************************************************************")
#definindo a palavra secreta
palavra_secreta = 'banana'
#print(type(palavra_secreta))
acertou = False
enforcou = False
#lista para guardar os valores
letras_acertadas = ['_', '_', '_', '_', '_', '_']

print(letras_acertadas)
while(not enforcou and not acertou):
    chute = input("Qual letra? ")

    posicao = 0
    for letra, in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
#           print("Encontrei a letra {} na posição {}".format(letra, posicao))
        posicao = posicao + 1
    print(letras_acertadas)
#    print("Jogando...")

print("Fim do Jogo!")

