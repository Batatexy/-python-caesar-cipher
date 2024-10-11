import os  # Biblioteca para limpar o terminal

# Função de criptografia que será usada mais pra frente no código
def criptografia(frase):  
    mensagem = ""  # Necessário reiniciar esta variável da função, para não criptografar um código antigo
    for i in frase:  # O i é responsável por navegar pelas letras da mensagem digitada
        if sinal == "+":  # Utilização de uma variável que determina se as letras irão mudar pra frente ou para trás
            mensagem += chr(ord(i) + casas)
        else:  # Os dois comandos que voltam ou avançam cada uma das letras, comandado pelo i, da mensagem para criptografa-lo
            mensagem += chr(ord(i) - casas)
    return mensagem  # Retornar a mensagem descriptografada de volta para uma variável determinada no parâmetro

# Função de criptografia que será usada mais pra frente no código
def descriptografia(frase):
    mensagem = ""  # Necessário reiniciar esta variável da função, para não criptografar um código antigo
    for i in frase:  # O i é responsável por navegar pelas letras da mensagem criptografada
        if sinal == "+":  # Utilização de uma variável que determina se as letras irão mudar pra frente ou para trás
            mensagem += chr(ord(i) - casas)
        else:  # Os dois comandos que voltam ou avançam cada uma das letras, comandado pelo i, do texto criptografado para revelar a mensagem de volta
            mensagem += chr(ord(i) + casas)
    return mensagem  # Retornar a mensagem descriptografada de volta para uma variável determinada no parâmetro

# Função usada apenas para verificar se a mensagem ultrapassa 128 caracteres
def limite(mensagem): 
    if len(mensagem) > 128: # Verifica se há mais que 128 caracteres
        mensagem = mensagem[:128] # Pegar os primeiros 128 caracteres
        print("A frase apresenta mais de 128 caracteres, portanto a frase será alterada para:", mensagem)
        continuar()

# Função para mostrar diversas opções com base na mensagem escrita
def bruto(frase):
    mensagem = ""
    # Acima de 50 é praticamente impossível, uns 30 até que funciona, mais ainda pode causar problemas, 20 é ok
    valor = 20

    print()
    # Montar diversas combinações para frente
    print("Combinações para frente:")
    for i in range(0, valor, 1):
        for j in frase: # O i é responsável por navegar pelas letras da mensagem digitada
            mensagem += chr(ord(j) + i)
        mensagem = mensagem[-len(frase):] # Necessário remover os caracteres iniciais, pois ele sempre soma com a mensagem anterior
        print(mensagem) # Printar as diversas opções

    mensagem = "" # Reiniciar a variável para a próxima tentativa

    print()
    # Montar diversas combinações para trás
    print("Combinações para trás:")
    for i in range(0, valor, 1):
        for j in frase:
            mensagem += chr(ord(j) - i) 
        mensagem = mensagem[-len(frase):]
        print(mensagem)

# Função para o usuário pressionar ENTER e limpar o terminal
def continuar():
    continuar = str(input("Pressione ENTER para continuar:"))
    os.system('cls') # Comando para limpar o terminal

# Variáveis globais usadas ao longo do código
sinal = "+" # Variável que indica se as letras do código irão mudar pra frente ou para trás, Sinais aceitos:(+/-)
casas = 3  # Variável que afeta quantos caracteres serão modificados, por exemplo se o valor de casas for 12: a letra: A --> M
escolha = 0 # Variável que determina as escolhas do usuário a seguir:

while escolha != "0":
    os.system('cls')
    print("Escolha uma das opções a seguir:")
    print("1. Criptografar uma frase.")
    print("2. Descriptografar uma frase.")
    print("3. Como funciona?")
    print("4. Força Bruta.")
    print("0. Sair do programa.")
    escolha = str(input())

    match escolha:
        case "1":
            os.system('cls')
            mensagem = str(input("Digite uma mensagem para criptografar: "))
            limite(mensagem) #Rodar a função de verificar se tem mais de 128 carácteres

            while True: # Fica no while enquanto o usuário não digitar "+" ou "-"
                os.system('cls')
                print("Digite uma mensagem para criptografar:", mensagem) # Repetir apenas por motivos estéticos, caso o usuário digite errado o sinal, o terminal apagará, 
                sinal = str(input("Digite se a chave SERÁ movida para FRENTE ou para TRÁS (+/-):")) # mas a mensagem inicial sempre está visível 
                if sinal == "+" or sinal == "-":                         
                    break
                else:
                    print("Sinal inválido")

            if sinal == "+":
                casas = int(input("Digite quantas casas deseja avançar: "))
            else:
                casas = int(input("Digite quantas casas deseja recuar: "))
            
            texto_criptografado = criptografia(mensagem) # Salvar o texto criptografado em uma variável, chamando a função e usando a mensagem digitada como parâmetro
            print()
            print("Mensagem criptografada:", texto_criptografado)
            print()
            continuar()
            
        case "2":
            os.system('cls')
            mensagem = str(input("Digite uma mensagem para descriptografar: "))
            limite(mensagem)

            while True:
                os.system('cls')
                print("Digite uma mensagem para descriptografar:", mensagem)
                sinal = str(input("Digite se a chave FOI movida para FRENTE ou para TRÁS (+/-):"))
                if sinal == "+" or sinal == "-":
                    break
                else:
                    print("Sinal inválido")
            
            if sinal == "+":
                casas = int(input("Digite quantas casas foram avançadas: "))
            else:
                casas = int(input("Digite quantas casas foram recuadas: "))

            texto_descriptografado = descriptografia (mensagem) # Salvar o texto criptografado em uma variável, chamando a função e usando a mensagem digitada como parâmetro
            print()
            print("Mensagem criptografada:", texto_descriptografado)
            print()
            continuar()

        case "3":
            os.system ('cls')
            print("A cifra de César é um dos tipos de criptografias mais simples que existem, onde se consiste") 
            print("em mover cada letra de uma frase para frente ou pra trás no alfabeto, respectivas vezes,") 
            print("formando uma nova frase criptografada, e para reverter, basta avançar na direção oposta.") 
            print()
            mensagem = str(input("Digite uma mensagem para criptografar: "))
            limite (mensagem)

            os.system ('cls')
            texto_criptografado = criptografia (mensagem) # Salvar o texto criptografado em uma variável, chamando a função e usando a mensagem digitada como parâmetro 
            casas = 3 # Resetar para explicar o funcionamento do código
            print("Neste exemplo, moveremos em", casas, "cada letra de uma palavra, onde:")
            print()
            if sinal == "+": #Verificar se estamos somando ou subtraindo para melhor visibilidade na execução do código
                print("Ao somar", casas, "em cada letra isolada temos:")
            else:
                print("Ao subtrair", casas, "em cada letra isolada temos:")
            print("Texto Criptografado:", texto_criptografado) #Mostrar na tela o texto criptografado

            texto_descriptografado = descriptografia (texto_criptografado) #Mesma coisa que a criptografia, mas chamando a outra função e usando de parâmetro o texto criptografado
            print()
            if sinal == "+": #Verificar se estamos somando ou subtraindo para melhor visibilidade na execução do código 
                print("Subtraindo", casas, "em cada carácter, voltamos a mensagem original:")
            else:
                print("Somando", casas, "em cada carácter voltamos a mensagem original:")

            print("Texto Descriptografado:", texto_descriptografado) #Mostrar na tela o texto descriptografado

            print()
            print("Note, que o programa também aceita números e outros caracteres, pois como no computador") 
            print("existem diversos outros carácteres, também há uma ordem especifica para eles.") 
            print()
            continuar()
            
            print("E é assim que funciona uma cifra de César, mas ela é usada apenas para fins didáticos,") 
            print("já para a segurança de dados, há diversas outras criptografias melhores.")
            print()
            continuar()

        case "4":
            mensagem = str(input("Digite uma mensagem para mostrar várias opções de descriptografia: "))
            limite(mensagem)
            bruto(mensagem) # Chamar a função de força bruta
            continuar()

print("Fim do programa")