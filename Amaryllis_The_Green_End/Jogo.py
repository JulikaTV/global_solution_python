##############################################################################

# Avalia com carinho professor a gente deu a vida por ele <3

##############################################################################

# Integrantes do grupo:

# Gabriela Queiroga          560035
# Julia Sayuri Yokoo         560541
# Maria Eduarda Ferrés       560418

####################################################################################


# Inventário inicial da personagem

# Listas feitas para inventario

# Inicializa o inventário como duas listas paralelas
inventario = ['café', 'restos organicos', 'ferro', 'vidros', 'biogás', 'painel solar', 'celulas solares', 'remédios', 'madeiras']
qtd = [5, 3, 2, 1, 0, 0, 0, 0, 0]

# Função para exibir o inventário
def mostrar_inventario(inventario, qtd):
    print("\nInventário:")
    for i in range(len(inventario)):
        print(f"{inventario[i]}: {qtd[i]}")

# Função para adicionar ou atualizar itens no inventário
def itens_coletados(item, quantidade, inventario, qtd):
    encontrado = False
    for i in range(len(inventario)):
        if inventario[i] == item:
            qtd[i] += quantidade
            encontrado = True
            break
    if not encontrado:
        inventario.append(item)
        qtd.append(quantidade)

# Função para explorar e coletar itens
def caminhar(inventario, qtd):
    print("Deseja se aventurar?")
    resposta = input("sim ou não?\n-> ")

    if resposta == "sim":
        while True:
            print("\nEscolha para onde deseja ir:")
            print("1. Ruínas")
            print("2. Mercado Abandonado")
            print("3. Casa Abandonada")
            print("4. Farmácia Abandonada")
            print("5. Prédio Abandonado")
            escolha = input("Digite o número da sua escolha ou 'sair' para encerrar:\n-> ")

            if escolha == "1":
                print("Você está explorando as Ruínas!\n"
                      "Amaryllis: Escutei tantas histórias sobre essas ruínas antes do mundo virar cinza...\n"
                      "Amaryllis: Parece ter sido ontem o dia em que vi o papai chorando e relembrando de seus entes quridos...Sua antiga vida... e a mamãe o consolando.\n"
                      "Amaryllis: Eu era pequena demais para me lembrar do antes...\n\n")

                print("Você encontrou 1 ferro e uma bicicleta antiga.")
                itens_coletados("ferro", 1, inventario, qtd)
                itens_coletados("bicicleta antiga", 1, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "2":
                print("Você está explorando o Mercado Abandonado!\n"
                      "Amaryllis: É incrivel ainda ter sobrado algo\n"
                      "Amaryllis: ARGH!!! Eu detesto baratas!\n\n")

                print("Você encontrou 3 sacos de café.")
                itens_coletados("café", 3, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "3":
                print("Você está explorando a Casa Abandonada!\n"
                      "Amaryllis: Acho que tenho vagas memórias de como casas como essa apesar de simples eram bonitas e...aconchegantes...\n"
                      "Amaryllis: Fico imaginando como a minha poderia ficar parecida com essas em seu estado original\n"
                      "Amaryllis: Posso pegar inspirações para deixar o meu lar mais bonito e acochegante também!!! Maybe life is a strawbery (Mamãe que ensinou)\n\n")
                print("Você encontrou 2 plásticos, 4 restos organicos e 4 madeiras.")
                itens_coletados("plástico", 2, inventario, qtd)
                itens_coletados("restos organicos", 4, inventario, qtd)
                itens_coletados("madeiras", 4, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "4":
                print("Você está explorando a Farmácia Abandonada!\n\n"
                      "Amaryllis: É engraçado pensar que em um lugar tão sujo era referencia em questão de saúde. Nem parece que eu posso acabar pegando uma doença aqui. \n"
                      "Amaryllis: *Atrás do balcão* Cof* cof* Olá caro cliente! Como posso ajuda-lo?\n"
                      "Amaryllis: Talvez se a minha amiga Paty estivesse aqui fosse mais engraçado... Vou chamar ela para vir brincar aqui um dia desses!\n\n")
                
                print("Você encontrou 2 remédios, 4 restos organicos e 3 vidros.")
                itens_coletados("remédios", 2, inventario, qtd)
                itens_coletados("restos organicos", 4, inventario, qtd)
                itens_coletados("vidros", 3, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "5":
                print("Você está explorando o Prédio Abandonado!\n\n"
                      "Amaryllis: Incrível como elas mesmo derrubadas são ENORMES!!!\n"
                      "Amaryllis: Como deve ter sido er morado nelas ainda esguidas? Mamãe disse que nós morávamos em uma delas quando eu era muito pequena.\n"
                      "Amaryllis: Tudo parece ser tão pequeno daqui de cima...E...Insignificante.\n\n")
                
                print("Você encontrou 6 fios, 4 tubos e 1 balde verde.")
                itens_coletados("fios", 6, inventario, qtd)
                itens_coletados("tubos", 4, inventario, qtd)
                itens_coletados("balde verde", 1, inventario, qtd)
                mostrar_inventario(inventario, qtd)

            elif escolha == "sair":
                print("Encerrando exploração.")
                break

            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Talvez na próxima vez.")

# Função para criar biogás
def criar_biogas(inventario, qtd):
    tem_restos = False
    tem_fitas = False

    for i in range(len(inventario)):
        if inventario[i] == "restos organicos" and qtd[i] >= 3:
            tem_restos = True
            idx_restos = i
        elif inventario[i] == "fitas" and qtd[i] >= 1:
            tem_fitas = True
            idx_fitas = i

    if tem_restos and tem_fitas:
        qtd[idx_restos] -= 3
        qtd[idx_fitas] -= 1
        itens_coletados("biogás", 1, inventario, qtd)
        print("\nVocê criou 1 unidade de Biogás!")
    else:
        print("\nNão há materiais suficientes para criar Biogás.")

# Função para criar painel solar
def criar_painel_solar(inventario, qtd):
    tem_vidros = False
    tem_ferro = False

    for i in range(len(inventario)):
        if inventario[i] == "vidros" and qtd[i] >= 3:
            tem_vidros = True
            idx_vidros = i
        elif inventario[i] == "ferro" and qtd[i] >= 2:
            tem_ferro = True
            idx_ferro = i

    if tem_vidros and tem_ferro:
        qtd[idx_vidros] -= 3
        qtd[idx_ferro] -= 2
        itens_coletados("painel solar", 1, inventario, qtd)
        print("\nVocê criou 1 Painel Solar!")
    else:
        print("\nNão há materiais suficientes para criar um Painel Solar.")

# Função para simular o impacto da poluição
def simular_poluicao(inventario, qtd):
    reducao = 0
    for i in range(len(inventario)):
        if inventario[i] == "biogás":
            reducao += qtd[i] * 10
        elif inventario[i] == "painel solar":
            reducao += qtd[i] * 15

    print(f"\nA poluição foi reduzida em {reducao} unidades!")

# Função principal para rodar o jogo
def jogar():
    print("\nBem-vindo ao jogo de sobrevivência!")

    while True:
        print("\nEscolha uma ação:")
        print("1. Ver Inventário")
        print("2. Explorar")
        print("3. Criar Biogás")
        print("4. Criar Painel Solar")
        print("5. Simular Poluição")
        print("6. Sair do Jogo")

        escolha = input("Digite o número da sua escolha:\n-> ")

        if escolha == "1":
            mostrar_inventario(inventario, qtd)

        elif escolha == "2":
            caminhar(inventario, qtd)

        elif escolha == "3":
            criar_biogas(inventario, qtd)

        elif escolha == "4":
            criar_painel_solar(inventario, qtd)

        elif escolha == "5":
            simular_poluicao(inventario, qtd)

        elif escolha == "6":
            print("Saindo do jogo. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o jogo
jogar()