import os
from data import data_da_consulta
import datetime
from interface import parar_exibir, limpar_tela, linha

name_file = 'preços-produtos.txt'

def editar_arquivo_texto(list):
    """
    -> Insere os dados do produto no arquivo de texto
    Args:
        list: lista contendo informações do produto em seus elementos.
    """
    with open(name_file, 'at+') as produtos:
        produtos.seek(0)      # retorna o ponteiro de leitura do txt p/ o início
        num_id = len(produtos.readlines()) + 1
        produtos.write(str(num_id) + ';')
        for item in (list):
            produtos.write(str(item) + ';')
        data_hora = data_da_consulta()
        produtos.write(data_hora + '\n')
        limpar_tela()
    ler_arquivo(cod=list[1], operação=True)
        

def ler_arquivo(cod='', operação=False):
    """
    -> Faz a leitura do arquivo de texto e apresenta ao usuário os produtos
    """
    try:
        with open(name_file, 'r') as produtos:
            line = produtos.readlines()
            if len(line) == 0:
                return print('Nenhum produto foi cadastrado')

            if operação == True:
                list = []
                for i, item in enumerate(line):
                    item = item.replace('\n', '')
                    info = item.split(';')
                    if info[2] == cod:
                        list.append(line[i])
                if len(list) == 0:
                    print('Produto não encontrado. Tente ver a lista completa')
                else:
                    exibir_informação(list)
            else:
                exibir_informação(line)
    except (FileNotFoundError, IndexError):
        print('''\033[31mERROR:
        Possíveis causas e ações:
        Base de dados não existe.
        Verifique a integridade da base de dados, o arquivo pode ter sido alterado inadequadamente.\033[m''')
    parar_exibir()


def exibir_informação(list):
    print(f'\033[1;32m{"id":<4}{"Nome do Produto":<20}{"Cód.":<10}{"Lote":<10}{"Custo":<10}{"Margem de Lucro (%)":<25}{"Preço de venda":<12}{"Data da Consulta":>20} \033[m')
    linha()
    for item in list:
        item = item.replace('\n', '')
        info = item.split(';')
        print(f'{info[0]:<4}{info[1]:<20}{info[2]:<10}{info[3]:<10}R$ {info[4]:<10}{info[5]:^25}\033[1;31mR$ {info[6]:<12}\033[m{info[7]:<20}')
        linha()
    

def registrar_produtos():
    """
    -> Salva os dados do produto, incluindo seu preço de venda
    """
    dados = [str(input('Nome do produto: ')),
    str(input('Código do produto: ')),
    str(input('Lote: ')),
    float(input('Custo do produto: R$')),
    float(input('Margem de lucro [%]: '))
    ]
    preço = (dados[3] / (1 - (dados[4]/100))).__round__(2)
    dados.append(preço)
    editar_arquivo_texto(dados)

''' dados = []
    nome = str(input('Nome do produto: '))
    cod = str(input('Código do produto: '))
    lote = str(input('Lote: '))
    custo = float(input('Custo do produto: R$'))
    margem_lucro = float(input('Margem de lucro [%]: '))
    preço = (custo / (1 - (margem_lucro/100))).__round__(2)
    dados.append(nome)
    dados.append(cod)
    dados.append(lote)
    dados.append(custo)
    dados.append(margem_lucro)
    dados.append(preço)
    editar_arquivo_texto(dados)'''