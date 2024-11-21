#################################################################################################################################################################################################################

# Avalia com carinho professor a gente deu a vida por ele <3

#################################################################################################################################################################################################################

# Integrantes do grupo:

# Gabriela Queiroga          560035
# Julia Sayuri Yokoo         560541
# Maria Eduarda Ferrés       560418

##################################################################################################################################################################################################################

# Inventário inicial da personagem

# Listas feitas para inventário

# Inicializa o inventário como duas listas paralelas
inventario = ['café', 'restos organicos', 'ferro', 'vidros', 'biogás', 'painel solar', 'celulas solares', 'remédios', 'madeiras']
qtd = [5, 3, 2, 1, 0, 0, 0, 0, 0]

# Função para exibir o inventário
def mostrar_inventario(inventario, qtd):
    print("\nInventário:")
    for i in range(len(inventario)):
        print(f"{inventario[i]}: {qtd[i]}")

###################################################################################################################################################################################################################

# Função para adicionar ou atualizar itens no inventário

def itens_coletados(item, quantidade, inventario, qtd):

    # Como o item q personagem ainda não encontrou não esta dentro do inventário, então ele será considerado "Falso"
    encontrado = False

    # A "len" vai retornar o número de elementos da lista (inventario)
    # O "for" itera sobre a sequencia gerada pelo range 
    # O "range" vai gerar uma sequencia de números 
    # O "i" vai assumir o lugar de um índice da lista , começando por 0 e indo até o último índice
    for i in range(len(inventario)):

        # Se inventario[indice] igual ao item, então a quantidade encontrada sera adicionada ao inventario
        if inventario[i] == item:
            qtd[i] += quantidade

            # No momento que a personagem encontra o item ele se torna "True" ou seja, verdadeiro. 
            encontrado = True
            break
    if not encontrado:

        # Caso o item não seja encontrado

        # O append irá adicionar o item encontrado ao final da lista
        inventario.append(item)
        
        # O append irá adicionar a quantidade do item encontrado
        qtd.append(quantidade)

###################################################################################################################################################################################################################

# Função para explorar e coletar itens
def caminhar(inventario, qtd):

    # Mostra uma mensagem inicial perguntando se o jogador deseja explorar
    print("Deseja se aventurar?")
    resposta = input("sim ou não?\n-> ")  # Solicita uma resposta do jogador

    # Verifica se a resposta do jogador foi "sim"
    if resposta == "sim":

        # Enquanto o jogador não decidir sair, mantém o loop de exploração
        while True:

            # Mostra as opções de lugares para explorar
            print("\nEscolha para onde deseja ir:")
            print("1. Ruínas")
            print("2. Mercado Abandonado")
            print("3. Casa Abandonada")
            print("4. Farmácia Abandonada")
            print("5. Prédio Abandonado")
            escolha = input("Digite o número da sua escolha ou 'sair' para encerrar:\n-> ")  # Solicita a escolha do jogador

            # Verifica qual local o jogador escolheu explorar
            if escolha == "1":

                # Ruínas
                print("Você está explorando as Ruínas!\n"
                      "Amaryllis: Escutei tantas histórias sobre essas ruínas antes do mundo virar cinza...\n"
                      "Amaryllis: Parece ter sido ontem o dia em que vi o papai chorando e relembrando de seus entes queridos...Sua antiga vida... e a mamãe o consolando.\n"
                      "Amaryllis: Eu era pequena demais para me lembrar do antes...\n\n")

                # Mensagem informando os itens encontrados
                print("Você encontrou 1 ferro e uma bicicleta antiga.")
                
                # Adiciona o item "ferro" ao inventário com uma quantidade de 1
                # A função "itens_coletados" é chamada para verificar se o item já existe no inventário:
                # Se o item já existir, sua quantidade será incrementada.
                # Se o item não existir, ele será adicionado ao final do inventário junto com a quantidade especificada.

                itens_coletados("ferro", 1, inventario, qtd)

                # Adiciona o item "bicicleta antiga" ao inventário com uma quantidade de 1
                # O funcionamento é o mesmo do item anterior: verifica se o item já existe no inventário e, se não existir, o adiciona.

                itens_coletados("bicicleta antiga", 1, inventario, qtd)

                # Mostra o inventário atualizado na tela
                # A função "mostrar_inventario" exibe os itens do inventário junto com suas respectivas quantidades.
                # É útil para o jogador acompanhar os recursos coletados após cada exploração.

                mostrar_inventario(inventario, qtd)


            elif escolha == "2":

                # Mercado Abandonado
                print("Você está explorando o Mercado Abandonado!\n"
                      "Amaryllis: É incrível ainda ter sobrado algo\n"
                      "Amaryllis: ARGH!!! Eu detesto baratas!\n\n")

                # Mensagem informando os itens encontrados
                print("Você encontrou 3 sacos de café.")
               
                itens_coletados("café", 3, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "3":

                # Casa Abandonada
                print("Você está explorando a Casa Abandonada!\n"
                      "Amaryllis: Acho que tenho vagas memórias de como casas como essa, apesar de simples, eram bonitas e... aconchegantes...\n"
                      "Amaryllis: Fico imaginando como a minha poderia ficar parecida com essas em seu estado original\n"
                      "Amaryllis: Posso pegar inspirações para deixar o meu lar mais bonito e aconchegante também!!! Maybe life is a strawberry (Mamãe que ensinou)\n\n")

                # Mensagem informando os itens encontrados
                print("Você encontrou 2 plásticos, 4 restos orgânicos e 4 madeiras.")

                itens_coletados("plástico", 2, inventario, qtd)
                itens_coletados("restos organicos", 4, inventario, qtd)
                itens_coletados("madeiras", 4, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "4":

                # Farmácia Abandonada
                print("Você está explorando a Farmácia Abandonada!\n\n"
                      "Amaryllis: É engraçado pensar que em um lugar tão sujo era referência em questão de saúde. Nem parece que eu posso acabar pegando uma doença aqui. \n"
                      "Amaryllis: *Atrás do balcão* Cof* cof* Olá caro cliente! Como posso ajudá-lo?\n"
                      "Amaryllis: Talvez se a minha amiga Paty estivesse aqui fosse mais engraçado... Vou chamar ela para vir brincar aqui um dia desses!\n\n")
                
                # Mensagem informando os itens encontrados
                print("Você encontrou 2 remédios, 4 restos orgânicos e 3 vidros.")
                
                itens_coletados("remédios", 2, inventario, qtd)
                itens_coletados("restos organicos", 4, inventario, qtd)
                itens_coletados("vidros", 3, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "5":

                # Prédio Abandonado
                print("Você está explorando o Prédio Abandonado!\n\n"
                      "Amaryllis: Incrível como elas mesmo derrubadas são ENORMES!!!\n"
                      "Amaryllis: Como deve ter sido morar nelas ainda erguidas? Mamãe disse que nós morávamos em uma delas quando eu era muito pequena.\n"
                      "Amaryllis: Tudo parece ser tão pequeno daqui de cima... E... Insignificante.\n\n")
                
                # Mensagem informando os itens encontrados
                print("Você encontrou 6 fios, 4 tubos e 1 balde verde.")
                
                itens_coletados("fios", 6, inventario, qtd)
                itens_coletados("tubos", 4, inventario, qtd)
                itens_coletados("balde verde", 1, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "sair":

                # Encerra a exploração caso o jogador escolha "sair"
                print("Encerrando exploração.")
                break

            else:

                # Mensagem de erro para opções inválidas
                print("Opção inválida. Tente novamente.")
    else:

        # Caso o jogador escolha não explorar
        print("Talvez na próxima vez.")

################################################################################################################################################################################################################

# Função para criar biogás
def criar_biogas(inventario, qtd):
    # Variáveis para verificar a presença dos materiais necessários
    # # Indica se há restos orgânicos suficientes (mínimo de 3)
    tem_restos = False

    # Indica se há fitas suficientes (mínimo de 1)  
    tem_fitas = False  

    # Loop que percorre todos os itens no inventário
    for i in range(len(inventario)):

        # Verifica se há restos orgânicos suficientes (3 ou mais)
        if inventario[i] == "restos organicos" and qtd[i] >= 3:

            # Marca que há restos orgânicos suficientes
            tem_restos = True 

            # Armazena o índice do item "restos orgânicos"
            idx_restos = i  


        # Verifica se há fitas suficientes (1 ou mais)
        elif inventario[i] == "fitas" and qtd[i] >= 1:

            # Marca que há fitas suficientes
            tem_fitas = True  

            # Armazena o índice do item "fitas"
            idx_fitas = i  

    # Condicional que verifica se os materiais necessários estão presentes
    if tem_restos and tem_fitas:

        # Subtrai a quantidade necessária dos materiais no inventário
        # Remove 3 unidades de restos orgânicos
        qtd[idx_restos] -= 3  

        # Remove 1 unidade de fitas
        # Chama a função para registrar que o biogás foi criado
        qtd[idx_fitas] -= 1  

        # Mensagem de sucesso
        itens_coletados("biogás", 1, inventario, qtd)
        print("\nVocê criou 1 unidade de Biogás!")  

    else:

        # Caso não tenha materiais suficientes, exibe uma mensagem de erro
        print("\nNão há materiais suficientes para criar Biogás.")

#################################################################################################################################################################################################################

# Função para criar painel solar
def criar_painel_solar(inventario, qtd):

    # Variáveis para verificar a presença dos materiais necessários
    # Indica se há vidros suficientes (mínimo de 3)
    tem_vidros = False  

    # Indica se há ferro suficiente (mínimo de 2)
    tem_ferro = False  

    # Loop que percorre todos os itens no inventário
    for i in range(len(inventario)):

        # Verifica se há vidros suficientes (3 ou mais)
        if inventario[i] == "vidros" and qtd[i] >= 3:

            # Marca que há vidros suficientes
            tem_vidros = True 

            # Armazena o índice do item "vidros"
            idx_vidros = i 

        # Verifica se há ferro suficiente (2 ou mais)
        elif inventario[i] == "ferro" and qtd[i] >= 2:

            # Marca que há ferro suficiente
            tem_ferro = True  

            # Armazena o índice do item "ferro"
            idx_ferro = i  

    # Condicional que verifica se os materiais necessários estão presentes
    if tem_vidros and tem_ferro:

        # Subtrai a quantidade necessária dos materiais no inventário
        # Remove 3 unidades de vidros
        qtd[idx_vidros] -= 3
        
        # Remove 2 unidades de ferro
        qtd[idx_ferro] -= 2  

        # Chama a função para registrar que o painel solar foi criado
        itens_coletados("painel solar", 1, inventario, qtd)

        # Mensagem de sucesso
        print("\nVocê criou 1 Painel Solar!")  
    else:
        # Caso não tenha materiais suficientes, exibe uma mensagem de erro
        print("\nNão há materiais suficientes para criar um Painel Solar.")

###################################################################################################################################################################################################################

# Função para simular o impacto da poluição
def simular_poluicao(inventario, qtd):

    # Variável que acumula a redução da poluição
    reducao = 0  

    # Loop que percorre todos os itens no inventário
    for i in range(len(inventario)):

        # Se houver biogás, adiciona 10 de redução por unidade
        if inventario[i] == "biogás":

            # Cada unidade de biogás reduz 10 unidades de poluição
            reducao += qtd[i] * 10  

        # Se houver painel solar, adiciona 15 de redução por unidade
        elif inventario[i] == "painel solar":

            # Cada painel solar reduz 15 unidades de poluição
            reducao += qtd[i] * 15  

    # Exibe o impacto da poluição após o cálculo
    print(f"\nA poluição foi reduzida em {reducao} unidades!")
    
#######################################################################################################################################################################################################################

# Função principal para rodar o jogo
def jogar():
    # Exibe a mensagem de boas-vindas ao jogador
    print("\nBem-vindo ao jogo de sobrevivência!")

    # Loop principal do jogo - mantém o jogo em execução até o jogador decidir sair
    while True:

        # Menu principal do jogo com as opções disponíveis para o jogado
        print("\nEscolha uma ação:")

        # Opção para verificar os itens no inventário
        print("1. Ver Inventário")  

        # Opção para explorar o ambiente em busca de recursos
        print("2. Explorar")   

        # Opção para fabricar biogás usando recursos     
        print("3. Criar Biogás")    

        # Opção para construir um painel solar
        print("4. Criar Painel Solar")  

        # Opção para simular impactos ambientais
        print("5. Simular Poluição")    

        # Opção para encerrar o jogo
        print("6. Sair do Jogo")        

        # Solicita ao jogador que digite a sua escolha
        escolha = input("Digite o número da sua escolha:\n-> ")

        # Verifica a escolha do jogador
        if escolha == "1":

            # Chama a função para exibir o inventário e as quantidades dos itens
            mostrar_inventario(inventario, qtd)

        elif escolha == "2":

            # Chama a função para realizar a exploração do ambiente
            caminhar(inventario, qtd)

        elif escolha == "3":

            # Chama a função para fabricar biogás com base nos recursos disponíveis
            criar_biogas(inventario, qtd)

        elif escolha == "4":

            # Chama a função para construir um painel solar
            criar_painel_solar(inventario, qtd)

        elif escolha == "5":

            # Chama a função para simular os efeitos da poluição ambiental
            simular_poluicao(inventario, qtd)

        elif escolha == "6":

            # Encerra o jogo exibindo uma mensagem de despedida
            print("Saindo do jogo. Até mais!")
            break  # Sai do loop principal e encerra a função `jogar`

        else:

            # Caso o jogador insira um número inválido, exibe uma mensagem de erro
            print("Opção inválida. Tente novamente.")


# Iniciar o jogo
jogar()