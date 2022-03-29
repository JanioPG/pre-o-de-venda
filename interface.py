import os

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
    print('\033[36m-\033[m' * 119)

def display(list):
    print(f"\033[1;34m{'ID':<5} {'Code':<7} {'Name':<15} {'Batch':<8} {'Total cost':<12} {'Profit':<9} {'Sale price':<17}   {'Created at':<17}   {'Updated at':<15}\033[m")
    line()
    for value in list:
        id, code, name, batch, total_cost, profit_percentage, sale_price, created_at, updated_at = value
        print(f"{id:<5} {code:<7} {name:<15} {batch:<8} $ {str(round(total_cost, 2)):<10} {profit_percentage:.2f} {'%':<3} \033[32m$ {str(round(sale_price, 2)):<10}\033[m \033[36m|\033[m {str(created_at):<15} \033[36m|\033[m {str(updated_at):<15}")
        line()



def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def stop_showing():
    print('\nType \033[34mq\033[m to exit')
    while True:
        resp = str(input('Option:  ')).strip()
        if resp != 'q' or len(resp) == 0:
            continue
        else:
            break
    clean_screen()
