import interface
import arquivos

interface.limpar_tela()

while True:
    options = ['Preço de venda', 'Ver lista de produtos', 'Consultar único produto', 'Sair']
    interface.menu('Home', options)
    choice = str(input('Opção: ')).strip()
    interface.limpar_tela()
    if choice not in ['1', '2', '3', '4'] or choice == '':
        print('\033[31mOpção inválida. Escolha um número inteiro válido.\033[m')
        continue
    elif choice == '1':
        arquivos.registrar_produto()
    elif choice == '2':
        arquivos.ler_arquivo()
    elif choice == '3':
        while True:
            codigo = str(input('Informe o código do produto: ')).strip()
            interface.limpar_tela()
            if codigo == '':
                print('\033[31mERROR: Nenhum código informado.\033[m')
            else:
                break
        arquivos.ler_arquivo(codigo, operação=True)
    elif choice == '4':
        break
