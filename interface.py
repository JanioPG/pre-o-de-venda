import os
import keyboard

def header(text):
    print('\033[32m')
    print('=' * 50)
    print(text.center(50))
    print('=' * 50)
    print('\033[m')

def menu(text, list):
    header(text)
    for i, value in enumerate(list):
        print(f'[{i + 1}] {value}')

def linha():
    print('\033[36m-\033[m' * 114)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def parar_exibir():
    print('\nPressione \033[34mesc\033[m para sair')
    keyboard.wait('esc')
    limpar_tela()

