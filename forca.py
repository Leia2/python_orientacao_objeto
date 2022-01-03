#Jogo da adivinhação

print("*************************************************************************")
print("**************** Bem vindo ao jogo da Forca!*****************************")
print("*************************************************************************")
#definindo a palavra secreta
palavra_secreta = 'banana'
#print(type(palavra_secreta))
acertou = False
enforcou = False
erros = 0
#lista para guardar os valores
letras_acertadas = ['_', '_', '_', '_', '_', '_']


print(letras_acertadas)
while(not enforcou and not acertou):
    chute = input("Qual letra? ")

    if (chute in palavra_secreta):
        posicao = 0
        for letra, in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
    #           print("Encontrei a letra {} na posição {}".format(letra, posicao))
            posicao += 1
        
    else:
        erros +=1
        print("________________________________________________________________________")

        print("Você já possui {} erro".format(erros))
        print("________________________________________________________________________")
    acertou = '_' not in letras_acertadas
    enforcou = erros == 6
    #print("você já acertou", len(letras_acertadas))
    print(letras_acertadas)

if (acertou):
    print("Você ganhou!")

else:
    print("Você perdeu!") 
            
#    print("Jogando...")

print("Fim do Jogo!")

