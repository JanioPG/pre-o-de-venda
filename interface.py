import os


def header(texto):
    print('\033[32m')
    print('=' * 50)
    print(texto.center(50))
    print('=' * 50)
    print('\033[m')


def menu(texto, lista):
    header(texto)
    for i, value in enumerate(lista):
        print(f'[{i + 1}] {value}')


def linha():
    print('\033[36m-\033[m' * 114)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def parar_exibir():
    print('\nDigite \033[34mq\033[m para sair')
    while True:
        resp = str(input('Option:  ')).strip()
        if resp != 'q' or len(resp) == 0:
            return
        else:
            break
    limpar_tela()
