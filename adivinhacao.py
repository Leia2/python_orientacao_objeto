print('***********************************Jogo da Adivinhação**************')

#definindo a variável 
num_secreto = 42
total_tentativas = 0
nivel = 0
total_pontos = 1000
pontos_final = 0
#rodada = 1

"""while(rodada <=total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número: "))
    #Criando variáveis para armazenar as condições
    acertou = num_secreto == chute
    maior = chute > num_secreto
    menor = chute < num_secreto

    print("Você digitou", chute)
    if (acertou):
        print("Você acertou!")
        break
    elif(maior):
        print("Você errou, seu número foi maior do que o número secreto!")
    elif(menor):
        print("Você errou, seu chute foi menor que o número secreto")
    #total_tentativas = total_tentativas - 1
    rodada = rodada + 1"""

#Trabalhando com o for no lugar do while e usando a função range(inicio, fim, step) - o step 
# é opcional
#Se nivel = 1 total_tentativas = 20
nivel = int(input("Digite o seu nível, você pode escolher o nivel 1, 2 ou 3: "))
if nivel == 1:
    total_tentativas = 20
if (nivel == 2):
    total_tentativas = 10
if (nivel ==3):
    total_tentativas = 5

for rodada in range(1,total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um número: "))
    print("Você digitou {}".format(chute))
        
    acertou = num_secreto == chute
    maior = chute > num_secreto
    menor = chute < num_secreto  
    
    if (acertou):            
        print("Você acertou!")
        print("Sua pontaução atual é: ", abs(total_pontos))
        break
    elif(maior):
        aux = abs(chute - num_secreto)
        pontos_final = abs(total_pontos - aux)
    #    total_pontos = abs(pontos_final)
        print("Você errou, seu número foi maior do que o número secreto!")
        print("Sua pontaução atual é: ", abs(pontos_final))
        
    elif(menor):
        aux = abs(chute - num_secreto)
        print(aux)
        pontos_final = abs(total_pontos - aux)
        print(pontos_final)
    #    total_pontos = abs(pontos_final)
        print("Você errou, seu chute foi menor que o número secreto")
        print("Sua pontuação atual é: ", abs(pontos_final))
    total_pontos = pontos_final
print("Fim do jogo!")
