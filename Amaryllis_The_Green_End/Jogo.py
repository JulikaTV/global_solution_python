# Inventário inicial da personagem
inventario = {
    '\ncafé': 5,
    'restos de frutas': 3,
    'ferro': 2,
    'plástico': 1,
    'biogás': 0
}


# Função para exibir o inventário
def mostrar_inventario():
    print('\nInventário:')
    for item, quantidade in inventario.items():
        print(f'{item}: {quantidade}')


# Função para coletar um item e adicionar ao inventário
def coletar_item(item, quantidade):
    if item in inventario:
        inventario[item] += quantidade
    else:
        inventario[item] = quantidade
    print(f'Você coletou {quantidade} de {item}.')


# Função para criar biogás
def criar_biogas():
    if inventario['restos de frutas'] >= 3 and inventario['ferro'] >= 1:
        inventario['restos de frutas'] -= 3
        inventario['ferro'] -= 1
        inventario['biogás'] += 1
        print('\nParabéns! Você criou 1 unidade de Biogás!')
    else:
        print('\nNão há materiais suficientes para criar biogás.')


# Função para criar painel solar
def criar_painel_solar():
    if (inventario['plástico'] >= 1 and inventario['ferro'] >= 2):
        inventario['plástico'] -= 1
        inventario['ferro'] -= 2
        print('\nParabéns! Você criou um painel solar!')
    else:
        print('\nNão há materiais o suficientes para criar um painel solar.')


# Função para conversar com NPCs
def conversar(escolha_personagem):
    if escolha_personagem == 'velho_sabio':
        print('\nVelho Sábio: Você quer aprender a fazer energia limpa, certo?')
        resposta = input('\nVocê quer saber mais? (sim / não): ')
        if resposta == 'sim':
            print('\nVelho Sábio: Para criar biogás, use restos de frutas e ferro.')
            print('Velho Sábio: Para criar um painel solar, use plástico e ferro.')
        else:
            print('\nVelho Sábio: Então siga em frente, minha jovem.')
    else:
        print('\nEsse NPC não soube o que dizer.')


# Função para simular o impacto da poluição
def simular_poluicao():
    if inventario['biogás'] > 0:
        print('\nVocê usou o biogás! A qualidade do ar pode melhorar um pouco ao passar do tempo.')
        inventario['biogás'] -= 1  # Cada uso de biogás melhora o ar e consome um item
    else:
        print('\nA poluição continua alta! O ar está ficando cada vez ficando mais poluído.')


# Função principal do jogo
def jogar():
    print('\n ⠈⠂⠄⠄⠂⠁𝙱𝚎𝚖-𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝚓𝚘𝚐𝚘 𝚍𝚎 𝙰𝚖𝚊𝚛𝚢𝚕𝚕𝚒𝚜:The Green End⠈⠂⠄⠄⠂⠁')

    while True:
        print('\nQual ação gostaria de realizar?\n')
        print('1. Ver Inventário')
        print('2. Coletar materiais')
        print('3. Criar Biogás')
        print('4. Criar um Painel Solar')
        print('5. Conversar com o Velho Sábio')
        print('6. Simular quantidade de poluição')
        print('7. Sair do Jogo')

        escolha = input('Escolha uma opção (1-7)\n-> ').strip()

        if escolha == '1':
            mostrar_inventario()

        elif escolha == '2':
            item = input('\nQual item você gostaria de coletar?\n->').strip().lower()
            quantidade = int(input(f'\nQuantas unidades do {item}, você deseja coletar?\n->'))
            coletar_item(item, quantidade)

        elif escolha == '3':
            criar_biogas()

        elif escolha == '4':
            criar_painel_solar()

        elif escolha == '5':
            conversar('velho_sabio')

        elif escolha == '6':
            simular_poluicao()

        elif escolha == '7':
            print('Saindo do jogo 🔄')
            break

        else:
            print('\nOpção inválida, digite novamente alguma das opções!')


# Iniciar o jogo
jogar()