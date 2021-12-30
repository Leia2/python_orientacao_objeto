#Jogo da adivinhação

print("*************************************************************************")
print("**************** Bem vindo ao jogo da Forca!*****************************")
print("*************************************************************************")
#definindo a palavra secreta
palavra_secreta = 'banana'
#print(type(palavra_secreta))
acertou = False
enforcou = False

while(not enforcou and not acertou):
    chute = input("Qual letra? ")
    posicao = 0

    for letra, in palavra_secreta:
        if (chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição {}".format(letra, posicao))
        posicao = posicao + 1
    print("Jogando...")

print("Fim do Jogo!")
