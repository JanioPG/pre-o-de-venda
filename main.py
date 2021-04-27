from interface import *
from arquivos import *
import os

limpar_tela()

while True:
    opções = ['Preço de venda', 'Ver lista de produtos', 'Consultar único produto', 'Sair']
    menu('Home', opções)
    escolha = str(input('Opção: ')).strip()
    os.system('cls' if os.name=='nt' else 'clear')
    if escolha == '1':
        registrar_produtos()
    elif escolha == '2':
        ler_arquivo()
    elif escolha == '3':
        while True:
            codigo = str(input('Informe o código do produto: ')).strip()
            limpar_tela()
            if codigo == '':
                print('\033[31mERROR: Nenhum código informado.\033[m')
            else:
                break
        ler_arquivo(codigo, operação=True)
    elif escolha == '4':
        break
    elif escolha not in '1234' or escolha == '':
        print('\033[31mOpção inválida. Escolha um número inteiro válido.\033[m')
        continue