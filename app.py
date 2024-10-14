import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    """
    Exibe o nome do programa no console.

    Esta função imprime o nome do programa em um formato estilizado, ajudando a
    identificar a aplicação ao usuário.
    """
    print(""" 
    Sabor Expresso
""")

def exibir_opcoes():
    """
    Exibe as opções disponíveis para o usuário.

    Esta função imprime no console uma lista de opções que o usuário pode escolher,
    facilitando a interação com o programa.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    """
    Finaliza a aplicação.

    Esta função é responsável por encerrar o programa, imprimindo uma mensagem de
    encerramento ao usuário.
    """
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    """
    Permite que o usuário volte ao menu principal.

    Esta função aguarda a entrada do usuário para retornar ao menu principal do
    programa.
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    """
    Informa o usuário sobre uma opção inválida.

    Esta função exibe uma mensagem de erro quando o usuário seleciona uma opção que
    não é válida, orientando-o a escolher uma opção correta.
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """
    Exibe um subtítulo no console.

    Args:
        texto (str): O texto a ser exibido como subtítulo.

    Esta função imprime o texto fornecido, formatando-o para ser reconhecido
    como um subtítulo, ajudando a organizar visualmente a saída do programa.
    """
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante.

    Esta função solicita ao usuário as informações necessárias para cadastrar um novo
    restaurante no sistema, validando os dados antes de adicioná-los à lista de restaurantes.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados.

    Esta função percorre a lista de restaurantes cadastrados e imprime suas informações
    no console, permitindo ao usuário visualizar os restaurantes disponíveis.
    """
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """
    Alterna o estado (ativo/inativo) de um restaurante.

    Esta função permite ao usuário selecionar um restaurante e alterar seu estado de
    ativo para inativo ou vice-versa, atualizando a lista de restaurantes conforme necessário.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

def escolher_opcao():
    """
    Permite ao usuário escolher uma opção do menu.

    Esta função exibe as opções disponíveis e solicita ao usuário que escolha uma
    delas, retornando a opção selecionada para ser utilizada em outras partes do programa.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """
    Função principal que controla o fluxo do programa.

    Esta função orquestra a execução das demais funções, permitindo que o usuário
    interaja com o programa, escolhendo opções e realizando operações como cadastrar,
    listar e alternar estados de restaurantes.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
