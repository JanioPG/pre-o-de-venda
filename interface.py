import os
from venv import create


def header(text):
    print('\033[32m')
    print('=' * 50)
    print(text.center(50))
    print('=' * 50)
    print('\033[m')


def menu(text, list, message):
    header(text)
    for i, value in enumerate(list):
        print(f'[{i + 1}] {value}')
    print(f"\033[31m{message}\033[m")


def line():
    print('\033[36m-\033[m' * 114)

def display(list):
    print(f"\033[1;34m{'ID':<5} {'Code':<7} {'Name':<15} {'Batch':<10} {'Total cost':<15} {'Profit':<7} {'Sale price':<7}   {'Created at':<15}   {'Updated at':<15}\033[m")
    line()
    for value in list:
        id, code, name, batch, total_cost, profit_percentage, sale_price, created_at, updated_at = value
        print(f"{id:<5} {code:<7} {name:<15} {batch:<10} $ {str(total_cost):<10} {str(profit_percentage):>7} % $ {str(sale_price):<10} | {str(created_at):<15} | {str(updated_at):<15}")
        line()



def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def stop_showing():
    print('\nType \033[34mq\033[m to exit')
    while True:
        resp = str(input('Option:  ')).strip()
        if resp != 'q' or len(resp) == 0:
            return
        else:
            break
    clean_screen()
